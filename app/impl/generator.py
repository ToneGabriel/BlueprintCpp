from .. import config
from typing import Any
from importlib.resources import files
from jinja2 import Environment, FileSystemLoader


_GENERATION_ENVIRONMENT = Environment(loader=FileSystemLoader(str(files(config.TEMPLATES_DIR))),
                                      trim_blocks=True,
                                      lstrip_blocks=True
                                      )

_TEMPLATE_H = _GENERATION_ENVIRONMENT.get_template(config.HEADER_TEMPLATE_FILE)
_TEMPLATE_CPP = _GENERATION_ENVIRONMENT.get_template(config.SOURCE_TEMPLATE_FILE)


def generate_header_content(module: dict[str, Any]) -> str:
    return _TEMPLATE_H.render(module=module)


def generate_source_content(module: dict[str, Any]) -> str:
    return _TEMPLATE_CPP.render(module=module)

