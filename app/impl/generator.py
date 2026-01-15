import yaml
from typing import Any
from pathlib import Path
from jinja2 import Environment, PackageLoader


class CppGenerator:
    _INDENT = "    "
    _STEREOTYPES = {"virtual", "virtual_0", "override", "const", "noexcept"}

    def __init__(self,
                 jinja_env_package: str,
                 header_template_filename: str,
                 source_template_filename: str
                 ):

        self.env = Environment(loader=PackageLoader(jinja_env_package),
                               trim_blocks=True,
                               lstrip_blocks=True
                               )
        self.template_h = self.env.get_template(header_template_filename)
        self.template_cpp = self.env.get_template(source_template_filename)
        self.model = None

    def load_model(self, yaml_path: Path) -> None:
        data = yaml.safe_load(yaml_path.read_text())
        self.model = self._parse_yaml(data)

    def generate_header_content(self) -> str:
        if self.model:
            return self.template_h.render(model=self.model, indentation=CppGenerator._INDENT)

    def generate_source_content(self) -> str:
        if self.model:
            return self.template_cpp.render(model=self.model, indentation=CppGenerator._INDENT)

    def _parse_yaml(self, data: dict[str, Any]) -> dict[str, Any]:
        # Base structure
        model = {
                    "name": data.get("name", "_DefaultClass"),
                    "type": data.get("type", "Class"),
                    "description": data.get("description", None),
                    "namespaces": data.get("namespaces", []),
                    "include_guard": "",
                    "includes": data.get("includes", []),
                    "inherits": data.get("inherits", []),
                    "members": {
                                    "public": [],
                                    "protected": [],
                                    "private": []
                                },
                    "methods": {
                                    "public": [],
                                    "protected": [],
                                    "private": []
                                }
                }

        # Include Guard
        include_guard_parts = model["namespaces"] + [model["name"], "H"]
        model["include_guard"] = "_".join(p.upper() for p in include_guard_parts)

        # Members
        for m in data.get("members", []):
            visibility = m.get("visibility", "private")

            model["members"][visibility].append({
                                                    "name": m.get("name", "_defaultMember"),
                                                    "type": m.get("type", "void"),
                                                    "description": m.get("description", None)
                                                })

        # Methods
        for m in data.get("methods", []):
            visibility = m.get("visibility", "public")

            model["methods"][visibility].append({
                                                    "name": m.get("name", "_DefaultMethod"),
                                                    "return_type": m.get("return_type", None),
                                                    "params":   [
                                                                    {
                                                                        "name": p.get("name", "_param"),
                                                                        "type": p.get("type", "void")
                                                                    } for p in m.get("params", [])
                                                                ],
                                                    "stereotypes":  {
                                                                        s: (s in m.get("stereotypes", [])) for s in CppGenerator._STEREOTYPES
                                                                    },
                                                    "description": m.get("description", None)
                                                })

        return model
