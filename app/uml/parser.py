import re
from pathlib import Path
from collections import defaultdict

# -------------------------------
# Constants & helpers
# -------------------------------

VISIBILITY_MAP = {
    '+': 'public',
    '-': 'private',
    '#': 'protected'
}

KNOWN_STEREOTYPES = {
    "virtual",
    "virtual_0",
    "override",
    "const",
    "noexcept"
}

ARROW_RELATION = {
    '--|>': 'inherits',
    '<|--': 'inherits',
    '..|>': 'implements',
    '<|..': 'implements'
}


def normalize_qualified(name: str) -> str:
    return name.replace('.', '::')


# -------------------------------
# Main parser
# -------------------------------

class UmlModelParser:
    def __init__(self):
        self.model = {}
        self.current_file = None

    # ---------- public API ----------

    def parse_directory(self, root: Path) -> dict:
        for puml in root.rglob("*.puml"):
            self.current_file = str(puml)
            self._parse_file(puml)
        return self.model

    # ---------- file parsing ----------

    def _parse_file(self, path: Path):
        block_stack = []  # ("namespace" | "class" | "interface", name)

        with path.open(encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.strip()

                if not line or line.startswith("'"):
                    continue

                # -------------------------
                # Namespace start
                # -------------------------
                ns_match = re.match(r'namespace\s+(\w+)\s*\{', line)
                if ns_match:
                    block_stack.append(("namespace", ns_match.group(1)))
                    continue

                # -------------------------
                # Class / interface start
                # -------------------------
                decl_match = re.match(
                    r'(class|interface)\s+(\w+)'
                    r'(?:\s+extends\s+([\w:.]+))?'
                    r'(?:\s+implements\s+([\w:.,\s]+))?'
                    r'\s*\{?',
                    line
                )

                if decl_match:
                    kind, name, base, impls = decl_match.groups()
                    namespaces = self._current_namespaces(block_stack)

                    self._ensure_item(name, kind, namespaces)
                    block_stack.append((kind, name))   # ALWAYS push

                    item = self.model[name]

                    if base:
                        item["inherits"].append(normalize_qualified(base))

                    if impls:
                        for i in impls.split(","):
                            item["implements"].append(
                                normalize_qualified(i.strip())
                            )
                    continue

                # -------------------------
                # Arrow inheritance
                # -------------------------
                arrow_match = re.match(
                    r'(\w+)\s*([-.<|]{3,})\s*(\w+)', line
                )

                if arrow_match:
                    src, arrow, dst = arrow_match.groups()

                    self._ensure_item(src)
                    self._ensure_item(dst)

                    dst_type = self.model[dst]["type"]
                    relation = ARROW_RELATION.get(arrow, "inherits")

                    if relation == "implements" or dst_type == "interface":
                        self.model[src]["implements"].append(dst)
                    else:
                        self.model[src]["inherits"].append(dst)

                    continue

                # -------------------------
                # Members / methods
                # -------------------------
                member_match = re.match(r'([+\-#])\s*(.+)', line)
                if member_match:
                    visibility, body = member_match.groups()
                    current_class = self._current_class(block_stack)
                    if current_class:
                        self._parse_member_or_method(
                            current_class,
                            VISIBILITY_MAP[visibility],
                            body
                        )
                    continue

                # -------------------------
                # Block end
                # -------------------------
                if line == "}":
                    if block_stack:
                        block_stack.pop()
                    continue

    # ---------- model helpers ----------

    def _ensure_item(self, name, kind="class", namespaces=None):
        if name not in self.model:
            self.model[name] = {
                "type": kind,
                "namespaces": list(namespaces or []),
                "include_guard": self._make_guard(name, namespaces),
                "inherits": [],
                "implements": [],
                "members": defaultdict(list),
                "methods": defaultdict(list),
                "source_files": []
            }

        if self.current_file not in self.model[name]["source_files"]:
            self.model[name]["source_files"].append(self.current_file)

    def _make_guard(self, name, namespaces):
        parts = (namespaces or []) + [name, "H"]
        return "_".join(p.upper() for p in parts)

    # ---------- parsing helpers ----------

    def _current_namespaces(self, stack):
        return [n for t, n in stack if t == "namespace"]

    def _current_class(self, stack):
        for t, n in reversed(stack):
            if t in ("class", "interface"):
                return n
        return None

    def _parse_member_or_method(self, class_name, visibility, text):
        stereotypes = set(re.findall(r'<<(\w+)>>', text))
        text = re.sub(r'<<\w+>>', '', text).strip()

        # ---- method ----
        if '(' in text and ')' in text:
            left, right = text.split('(', 1)
            params = right.split(')')[0]

            parts = left.strip().split()
            name = parts[-1]
            return_type = " ".join(parts[:-1]) or "void"

            self.model[class_name]["methods"][visibility].append({
                "return_type": return_type,
                "name": name,
                "params": [p.strip() for p in params.split(',') if p.strip()],
                "stereotypes": {
                    s: s in stereotypes for s in KNOWN_STEREOTYPES
                }
            })
        # ---- member ----
        else:
            self.model[class_name]["members"][visibility].append(text)


# -------------------------------
# Example usage
# -------------------------------

if __name__ == "__main__":
    parser = UmlModelParser()
    model = parser.parse_directory(Path("."))

    # Debug print
    import pprint
    pprint.pprint(model)
