from clang import cindex
from collections import defaultdict
import os

# === Step 0: configure libclang path if needed ===
# cindex.Config.set_library_file("/usr/lib/llvm-14/lib/libclang.so.1")  # Linux
cindex.Config.set_library_file("/usr/lib/llvm-14/lib/libclang.so.1")
# cindex.Config.set_library_file("/usr/lib/llvm-17/lib/libclang.so")  # Linux
# cindex.Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")  # Windows

index = cindex.Index.create()

# === Helper: extract brief comment and @param descriptions ===
def extract_comments(cursor):
    brief = cursor.brief_comment or ""
    param_desc = {}
    if cursor.raw_comment:
        for line in cursor.raw_comment.splitlines():
            line = line.strip()
            if line.startswith("@param"):
                parts = line.split()
                if len(parts) >= 3:
                    param_name = parts[1]
                    desc = " ".join(parts[2:])
                    param_desc[param_name] = desc
    return brief, param_desc

# === Helper: get method "stereotypes" ===
def get_stereotypes(cursor):
    s = set()
    if cursor.is_const_method():
        s.add("const")
    if cursor.is_pure_virtual_method():
        s.add("virtual_0")
    if cursor.is_virtual_method() and not cursor.is_pure_virtual_method():
        s.add("virtual")
    if cursor.exception_specification_kind != cindex.ExceptionSpecificationKind.NONE:
        s.add("noexcept")
    # libclang does not directly expose 'override', but you can check overridden cursors
    if list(cursor.get_overridden_cursors()):
        s.add("override")
    return s

# === Helper: extract function body as raw string ===
def get_body_text(cursor):
    extent = cursor.extent
    if extent.start.file is None:
        return ""  # skip macros
    with open(extent.start.file.name, "r", encoding="utf-8") as f:
        text = f.read()
    return text[extent.start.offset:extent.end.offset]

# === Recursive AST walk ===
def parse_cursor(cursor, namespace_prefix=None):
    namespace_prefix = namespace_prefix or []

    results = {}

    # Track namespace
    if cursor.kind == cindex.CursorKind.NAMESPACE:
        new_prefix = namespace_prefix + [cursor.spelling]
        for c in cursor.get_children():
            child_results = parse_cursor(c, new_prefix)
            results.update(child_results)
        return results

    # Track classes
    if cursor.kind == cindex.CursorKind.CLASS_DECL and cursor.is_definition():
        class_name = "::".join(namespace_prefix + [cursor.spelling])
        class_dict = {
            "name": cursor.spelling,
            "namespaces": namespace_prefix,
            "inherits": [b.spelling for b in cursor.get_children() if b.kind == cindex.CursorKind.CXX_BASE_SPECIFIER],
            "destructor": None,
            "constructors": [],
            "members": [],
            "methods": [],
            "brief": cursor.brief_comment or "",
        }

        for c in cursor.get_children():
            # Fields
            if c.kind == cindex.CursorKind.FIELD_DECL:
                brief, _ = extract_comments(c)
                class_dict["members"].append({
                    "name": c.spelling,
                    "type": c.type.spelling,
                    "visibility": c.access_specifier.name.lower(),
                    "brief": brief,
                })

            # Constructors
            elif c.kind == cindex.CursorKind.CONSTRUCTOR:
                brief, param_desc = extract_comments(c)
                params = [{"name": p.spelling, "type": p.type.spelling, "brief": param_desc.get(p.spelling,"")} for p in c.get_arguments()]
                class_dict["constructors"].append({
                    "params": params,
                    "stereotypes": list(get_stereotypes(c)),
                    "brief": brief,
                    "body": get_body_text(c),
                })

            # Destructor
            elif c.kind == cindex.CursorKind.DESTRUCTOR:
                brief, _ = extract_comments(c)
                class_dict["destructor"] = {
                    "stereotypes": list(get_stereotypes(c)),
                    "brief": brief,
                    "body": get_body_text(c),
                }

            # Methods
            elif c.kind == cindex.CursorKind.CXX_METHOD:
                brief, param_desc = extract_comments(c)
                params = [{"name": p.spelling, "type": p.type.spelling, "brief": param_desc.get(p.spelling,"")} for p in c.get_arguments()]
                class_dict["methods"].append({
                    "name": c.spelling,
                    "return_type": c.result_type.spelling,
                    "visibility": c.access_specifier.name.lower(),
                    "params": params,
                    "stereotypes": list(get_stereotypes(c)),
                    "brief": brief,
                    "body": get_body_text(c),
                })

        results[class_name] = class_dict

    # Recurse for children
    for c in cursor.get_children():
        child_results = parse_cursor(c, namespace_prefix)
        results.update(child_results)

    return results

# === Main parse function ===
def parse_files(file_paths, compile_args=None):
    compile_args = compile_args or ["-std=c++20"]
    combined_results = {}
    for f in file_paths:
        # tu = index.parse(f, args=compile_args)
        tu = index.parse(f, args=compile_args, options=cindex.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD)
        for diag in tu.diagnostics:
            print(diag)
        file_results = parse_cursor(tu.cursor)
        combined_results.update(file_results)
    return combined_results

# === Example usage ===
if __name__ == "__main__":
    files = ["generated/test.h", "generated/test.cpp"]
    result_dict = parse_files(files, compile_args=["-std=c++20", "-Iinclude"])
    import pprint
    pprint.pprint(result_dict)

