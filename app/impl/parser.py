from .model import Stereotype, Visibility, ParameterType, Inheritance, Parameter, Method, Model
import yaml
from typing import Any


class Parser:
    def __init__(self,
                 standard_include_map: dict[str, str],
                 project_include_map: dict[str, str]
                 ):

        self._standard_include_map: dict[str, str]  = standard_include_map
        self._project_include_map: dict[str, str]   = project_include_map
        self._model: Model                          = None

    def set_model(self, model: Model) -> None:
        self._model = model

    def parse_yaml(self, yaml_text: str) -> None:
        data = yaml.safe_load(yaml_text)

        self._model.set_description(data.get("description", "Model description"))

        # model inheritances
        for i in data.get("inherits", []):
            inheritance = Inheritance(i.get("base", "void"), Visibility(i.get("visibility", "public")), i.get("virtual", False))
            self._model.add_inheritance(inheritance)
            self._check_includes(i.get("base", "void"))

        # model members
        for m in data.get("members", []):
            visibility = Visibility(m.get("visibility", "private"))

            member = Parameter(m.get("name", "_defaultMember"), m.get("description", "Member description"))

            # type
            mtype_data = m.get("type", {})
            mtype = ParameterType(mtype_data.get("name", "void"))
            for st in mtype_data.get("stereotypes", []):
                mtype.add_stereotype(Stereotype(st))
            member.set_type(mtype)
            self._check_includes(mtype_data.get("name", "void"))

            self._model.add_member(visibility, member)

        # model methods
        for m in data.get("methods", []):
            visibility = Visibility(m.get("visibility", "public"))

            method = Method(m.get("name", "_DefaultMethod"), m.get("description", "Method description"))

            # return type
            mret_type_data = m.get("type", {})
            mret_type = ParameterType(mret_type_data.get("name", "void"))
            for st in mret_type_data.get("stereotypes", []):
                mret_type.add_stereotype(Stereotype(st))
            method.set_type(mret_type)
            self._check_includes(mret_type_data.get("name", "void"))

            # parameters
            for p in m.get("params", []):
                param = Parameter(p.get("name", "_defaultParam"), p.get("description", "Parameter description"))

                # type
                ptype_data = p.get("type", {})
                ptype = ParameterType(ptype_data.get("name", "void"))
                for st in ptype_data.get("stereotypes", []):
                    ptype.add_stereotype(Stereotype(st))
                param.set_type(ptype)
                self._check_includes(ptype_data.get("name", "void"))

                method.add_parameter(param)

            self._model.add_method(visibility, method)

    def _check_includes(self, typedef: str) -> None:
        if (typedef in self._standard_include_map):
            self._model.add_system_include_h(self._standard_include_map[typedef])
        elif (typedef in self._project_include_map):
            self._model.add_project_include_h(self._project_include_map[typedef])
        else:
            pass
