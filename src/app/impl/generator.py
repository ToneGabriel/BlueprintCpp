from app.impl.model import Model
from jinja2 import Environment, PackageLoader, Template
from datetime import datetime, timezone


class CppGenerator:

    def __init__(self,
                 name_and_version: str,
                 jinja_env_package: str,
                 class_header_template_filename: str,
                 class_source_template_filename: str,
                 interface_header_template_filename: str,
                 enum_header_template_filename: str,
                 tab_indent: str
                 ):

        env: Environment = Environment(loader=PackageLoader(jinja_env_package),
                                       trim_blocks=True,
                                       lstrip_blocks=True
                                       )

        self._name_and_version: str = name_and_version
        self._tab_indent: str = tab_indent
        self._templates: dict[str, Template] = {
            "class_h":      env.get_template(class_header_template_filename),
            "class_cpp":    env.get_template(class_source_template_filename),
            "interface_h":  env.get_template(interface_header_template_filename),
            "enum_h":       env.get_template(enum_header_template_filename)
        }

    def generate_class_header_content(self, model: Model, source: str, file: str) -> str:
        return self._generate_content("class_h", model, source, file)

    def generate_class_source_content(self, model: Model, source: str, file: str) -> str:
        return self._generate_content("class_cpp", model, source, file)

    def generate_interface_header_content(self, model: Model, source: str, file: str) -> str:
        return self._generate_content("interface_h", model, source, file)

    def generate_enum_header_content(self, model: Model, source: str, file: str) -> str:
        return self._generate_content("enum_h", model, source, file)

    def _generate_content(self, kind: str, model: Model, source: str, file: str) -> str:
        return self._templates[kind].render(name_and_version=self._name_and_version,
                                            source=source,
                                            file=file,
                                            timestamp=datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                            tab=self._tab_indent,
                                            model=model.value
                                            )
