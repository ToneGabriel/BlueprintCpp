from .model import Model
from jinja2 import Environment, PackageLoader, Template


_TAB_INDENT = "    "


class CppGenerator:

    def __init__(self,
                 jinja_env_package: str,
                 header_template_filename: str,
                 source_template_filename: str
                 ):

        env: Environment = Environment(loader=PackageLoader(jinja_env_package),
                                       trim_blocks=True,
                                       lstrip_blocks=True
                                       )

        self._template_h: Template      = env.get_template(header_template_filename)
        self._template_cpp: Template    = env.get_template(source_template_filename)
        self._model: Model              = None

    def set_model(self, model: Model) -> None:
        self._model = model

    def generate_header_content(self) -> str:
        if self._model:
            return self._template_h.render(model=self._model.value, tab=_TAB_INDENT)

    def generate_source_content(self) -> str:
        if self._model:
            return self._template_cpp.render(model=self._model.value, tab=_TAB_INDENT)
