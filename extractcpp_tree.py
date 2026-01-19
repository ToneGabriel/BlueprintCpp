from pathlib import Path
from tree_sitter import Parser
from tree_sitter_languages import get_language, get_parser


# =========================
# Tree-sitter setup
# =========================


language = get_language('cpp')
parser = get_parser('cpp')


# =========================
# Helpers
# =========================

def node_text(node, source):
    return source[node.start_byte:node.end_byte].decode("utf-8")


def ensure_class(results, fq_name, namespaces, class_name):
    if fq_name not in results:
        results[fq_name] = {
            "name": class_name,
            "namespaces": namespaces.copy(),
            "inherits": [],
            "constructors": [],
            "destructor": None,
            "members": [],
            "methods": [],
            "brief": "",
        }
    return results[fq_name]


def split_qualified(name):
    parts = [p for p in name.split("::") if p]
    if len(parts) < 2:
        return None, name
    return "::".join(parts[:-1]), parts[-1]


# =========================
# Main parser
# =========================

def parse_cpp_file(path, results):
    source = Path(path).read_bytes()
    tree = parser.parse(source)
    root = tree.root_node

    namespace_stack = []

    def walk(node):
        nonlocal namespace_stack

        # -------- namespace --------
        if node.type == "namespace_definition":
            name = node.child_by_field_name("name")
            if name:
                namespace_stack.append(node_text(name, source))
                for c in node.children:
                    walk(c)
                namespace_stack.pop()
                return

        # -------- class / struct --------
        if node.type in ("class_specifier", "struct_specifier"):
            name_node = node.child_by_field_name("name")
            if not name_node:
                return

            class_name = node_text(name_node, source)
            fq_name = "::".join(namespace_stack + [class_name])

            cls = ensure_class(results, fq_name, namespace_stack, class_name)

            # inheritance
            base_clause = node.child_by_field_name("base_clause")
            if base_clause:
                for b in base_clause.children:
                    if b.type in ("type_identifier", "scoped_type_identifier"):
                        base = node_text(b, source)
                        if base not in cls["inherits"]:
                            cls["inherits"].append(base)

            # body
            body = node.child_by_field_name("body")
            if body:
                visibility = "private" if node.type == "class_specifier" else "public"

                for c in body.children:
                    if c.type == "access_specifier":
                        visibility = node_text(c, source)

                    elif c.type == "field_declaration":
                        decl = c.child_by_field_name("declarator")
                        typ = c.child_by_field_name("type")
                        if decl and typ:
                            cls["members"].append({
                                "name": node_text(decl, source),
                                "type": node_text(typ, source),
                                "visibility": visibility,
                                "brief": "",
                            })

                    elif c.type == "function_definition":
                        parse_method(
                            c, source, cls, class_name, visibility
                        )

        # -------- out-of-class method --------
        if node.type == "function_definition":
            declarator = node.child_by_field_name("declarator")
            if declarator:
                name_node = declarator.child_by_field_name("declarator")
                if name_node and name_node.type == "qualified_identifier":
                    full = node_text(name_node, source)
                    class_fq, method = split_qualified(full)
                    if class_fq and class_fq in results:
                        parse_method(
                            node,
                            source,
                            results[class_fq],
                            results[class_fq]["name"],
                            "unknown",
                        )

        for c in node.children:
            walk(c)

    walk(root)


def parse_method(node, source, cls, class_name, visibility):
    decl = node.child_by_field_name("declarator")
    body = node.child_by_field_name("body")

    if not decl:
        return

    name_node = decl.child_by_field_name("declarator")
    if not name_node:
        return

    name = node_text(name_node, source)

    params = []
    param_list = decl.child_by_field_name("parameters")
    if param_list:
        for p in param_list.children:
            if p.type == "parameter_declaration":
                pname = p.child_by_field_name("declarator")
                ptype = p.child_by_field_name("type")
                params.append({
                    "name": node_text(pname, source) if pname else "",
                    "type": node_text(ptype, source) if ptype else "",
                    "brief": "",
                })

    entry = {
        "name": name,
        "return_type": "",
        "visibility": visibility,
        "params": params,
        "stereotypes": [],
        "brief": "",
        "body": node_text(body, source) if body else "",
    }

    if name == class_name:
        cls["constructors"].append(entry)
    elif name.startswith("~"):
        cls["destructor"] = entry
    else:
        # avoid duplicates when merging h + cpp
        if not any(m["name"] == name for m in cls["methods"]):
            cls["methods"].append(entry)


# =========================
# Public API
# =========================

def parse_files(files):
    results = {}
    for f in files:
        parse_cpp_file(f, results)
    return results


# =========================
# Example usage
# =========================

if __name__ == "__main__":
    files = [
        "generated/test.h",
        "generated/test.cpp",
    ]

    result = parse_files(files)

    import pprint
    pprint.pprint(result)
