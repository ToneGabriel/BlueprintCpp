import yaml
from typing import Any
from pathlib import Path
from collections import defaultdict


def load_module_yaml(filepath: Path) -> dict[str, Any]:
    data = yaml.safe_load(filepath.read_text())

    # Base structure
    model = {
                "name": data.get("name", "_DefaultClass"),
                "type": data.get("type", "Class"),
                "description": data.get("description", ""),
                "namespaces": data.get("namespaces", []),
                "includes": data.get("includes", []),
                "inherits": data.get("inherits", []),
                "members": defaultdict(list),
                "methods": defaultdict(list)
            }

    # Split members/methods into separate visibilities for jinja
    model["members"] = {k: model["members"].get(k, []) for k in ["public", "protected", "private"]}
    model["methods"] = {k: model["methods"].get(k, []) for k in ["public", "protected", "private"]}

    # Members
    for m in data.get("members", []):
        visibility = m.get("visibility", "private")

        model["members"][visibility].append({
                                                "name": m.get("name", "_defaultMember"),
                                                "type": m.get("type", "void"),
                                                "description": m.get("description", "")
                                            })

    # Methods
    for m in data.get("methods", []):
        visibility = m.get("visibility", "public")

        model["methods"][visibility].append({
                                                "name": m.get("name", "_DefaultMethod"),
                                                "return_type": m.get("return_type", ""),
                                                "params":   [
                                                                {
                                                                    "name": p["name"],
                                                                    "type": p["type"]
                                                                } for p in m.get("params", [])
                                                            ],
                                                "stereotypes": m.get("stereotypes", []),
                                                "description": m.get("description", "")
                                            })

    return model
