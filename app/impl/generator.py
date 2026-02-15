from .model import Model
from jinja2 import Environment, PackageLoader, Template


_TAB_INDENT = "    "


class CppGenerator:

    def __init__(self,
                 jinja_env_package: str,
                 class_header_template_filename: str,
                 class_source_template_filename: str,
                 interface_header_template_filename: str,
                 enum_header_template_filename: str
                 ):

        env: Environment = Environment(loader=PackageLoader(jinja_env_package),
                                       trim_blocks=True,
                                       lstrip_blocks=True
                                       )

        self._class_template_h: Template        = env.get_template(class_header_template_filename)
        self._class_template_cpp: Template      = env.get_template(class_source_template_filename)
        self._interface_template_h: Template    = env.get_template(interface_header_template_filename)
        self._enum_template_h: Template         = env.get_template(enum_header_template_filename)

    def generate_class_header_content(self, model: Model) -> str:
        if model:
            return self._class_template_h.render(model=model.value, tab=_TAB_INDENT)

    def generate_class_source_content(self, model: Model) -> str:
        if model:
            return self._class_template_cpp.render(model=model.value, tab=_TAB_INDENT)

    def generate_interface_header_content(self, model: Model) -> str:
        if model:
            return self._interface_template_h.render(model=model.value, tab=_TAB_INDENT)

    def generate_enum_header_content(self,model: Model) -> str:
        if model:
            return self._enum_template_h.render(model=model.value, tab=_TAB_INDENT)
