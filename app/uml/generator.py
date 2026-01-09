import os
import sys
import re
from importlib.resources import files
from jinja2 import Environment, FileSystemLoader


# ------------------------
# Templates directory
# ------------------------
_GENERATION_ENVIRONMENT = Environment(loader=FileSystemLoader(str(files("templates"))),
                                      trim_blocks=True,
                                      lstrip_blocks=True
                                      )

_TEMPLATE_H = _GENERATION_ENVIRONMENT.get_template("class.h.j2")
_TEMPLATE_CPP = _GENERATION_ENVIRONMENT.get_template("class.cpp.j2")


# ------------------------
# Regexes to parse PlantUML
# ------------------------
RE_NAMESPACE = re.compile(r'namespace\s+(\w+)\s*{')
RE_CLASS = re.compile(r'(class|interface)\s+(\w+)\s*{?')
RE_MEMBER = re.compile(r'([+\-#])(\w+)\s*:\s*(.+)')
RE_METHOD = re.compile(r'([+\-#])(\w+)\s*\(([^)]*)\)\s*(<<[^>]+>>)?\s*(?::\s*(.+))?')
RE_INHERIT = re.compile(r'(\w+)\s*\.up\.\|>\s*(\w+(?:\.\w+)*)')


# ------------------------
# Data structures
# ------------------------
class Method:
    def __init__(self, name, ret, args, const=False, noexcept=False):
        self.name = name
        self.ret = ret
        self.args = args  # string with types
        self.const = const
        self.noexcept = noexcept

class Member:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_

class CppClass:
    def __init__(self, name, is_interface=False):
        self.name = name
        self.is_interface = is_interface
        self.members = {'public': [], 'protected': [], 'private': []}
        self.methods = {'public': [], 'protected': [], 'private': []}
        self.bases = []

# ------------------------
# Helper functions
# ------------------------
def parse_stereotypes(text):
    const = '<<const>>' in text if text else False
    noexcept = '<<noexcept>>' in text if text else False
    return const, noexcept

def parse_puml(filepath):
    namespaces = []
    classes = {}
    current_ns = None
    current_class = None
    visibility_map = {'+': 'public', '-': 'private', '#': 'protected'}

    with open(filepath) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith('@') or not line:
            continue

        # namespace
        ns_match = RE_NAMESPACE.match(line)
        if ns_match:
            current_ns = ns_match.group(1)
            namespaces.append(current_ns)
            continue

        # class/interface
        class_match = RE_CLASS.match(line)
        if class_match:
            kind, name = class_match.groups()
            cpp_class = CppClass(name, is_interface=(kind=='interface'))
            classes[name] = cpp_class
            current_class = cpp_class
            continue

        # member
        if current_class and ':' in line and '(' not in line:
            m = RE_MEMBER.match(line)
            if m:
                vis, name, type_ = m.groups()
                current_class.members[visibility_map[vis]].append(Member(name, type_))
            continue

        # method
        if current_class and '(' in line:
            m = RE_METHOD.match(line)
            if m:
                vis, name, args, stereotypes, ret = m.groups()
                const, noexcept = parse_stereotypes(stereotypes)
                ret = ret if ret else 'void'
                current_class.methods[visibility_map[vis]].append(Method(name, ret, args, const, noexcept))
            continue

        # inheritance
        inh = RE_INHERIT.match(line)
        if inh:
            derived, base = inh.groups()
            if derived in classes:
                # handle namespace-qualified base
                base_name = base.split('.')[-1]
                classes[derived].bases.append(base_name)
            continue

    return namespaces, classes

def generate_code(filepath, namespaces, classes):
    for cls_name, cpp_class in classes.items():
        # Skip forward declarations (interfaces with no members/methods)
        if cpp_class.is_interface and not cpp_class.methods['public']:
            continue

        include_guard = f"{cls_name.upper()}_H"

        h_template = _GENERATION_ENVIRONMENT.get_template("class.h.j2")
        cpp_template = _GENERATION_ENVIRONMENT.get_template("class.cpp.j2")

        # determine namespace path
        ns_path = [ns for ns in namespaces if ns]

        # render templates
        h_content = h_template.render(cpp_class=cpp_class, namespaces=ns_path, include_guard=include_guard)
        cpp_content = cpp_template.render(cpp_class=cpp_class, namespaces=ns_path)

        base_dir = os.path.dirname(filepath)
        h_path = os.path.join(base_dir, f"{cls_name}.h")
        cpp_path = os.path.join(base_dir, f"{cls_name}.cpp")

        with open(h_path, 'w') as f:
            f.write(h_content)
        with open(cpp_path, 'w') as f:
            f.write(cpp_content)
        print(f"Generated {h_path} and {cpp_path}")

# ------------------------
# Main
# ------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_cpp.py <file.puml>")
        sys.exit(1)

    puml_file = sys.argv[1]
    ns, classes = parse_puml(puml_file)
    generate_code(puml_file, ns, classes)
