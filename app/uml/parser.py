import yaml
from pathlib import Path
from collections import defaultdict


def load_class_yaml(path: Path):
    data = yaml.safe_load(path.read_text())

    # Base structure
    model = {
        "name": data.get("name", "_DefaultClass"),
        "namespaces": data.get("namespaces", []),
        "includes": data.get("includes", []),
        "inherits": data.get("inherits", []),
        "members": defaultdict(list),
        "methods": defaultdict(list)
    }

    # Members
    for m in data.get("members", []):
        vis = m.get("visibility", "private")
        model["members"][vis].append({
                                        "name": m.get("name", "_defaultMember"),
                                        "type": m.get("type", "void")
                                    })

    # Methods
    for m in data.get("methods", []):
        vis = m.get("visibility", "public")
        model["methods"][vis].append({
                                        "name": m.get("name", "_DefaultMethod"),
                                        "return_type": m.get("return_type", ""),
                                        "params": [{"name": p["name"], "type": p["type"]} for p in m.get("params", [])],
                                        "stereotypes": m.get("stereotypes", [])
                                    })

    # Split members/methods into separate visibilities for jinja
    model["members"] = {k: model["members"].get(k, []) for k in ["public", "protected", "private"]}
    model["methods"] = {k: model["methods"].get(k, []) for k in ["public", "protected", "private"]}

    return model


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    path = Path("class.yaml")
    cls_dict = load_class_yaml(path)
    from pprint import pprint
    pprint(cls_dict, width=120)
