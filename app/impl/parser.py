from .model import Stereotype, Visibility, ParameterType, Inheritance, Parameter, Method, EnumValue, Model
import yaml
from typing import Any


class Parser:
    def __init__(self,
                 standard_include_map: dict[str, str]
                 ):

        self._standard_include_map: dict[str, str]  = standard_include_map
        self._project_include_map: dict[str, str]   = {}
        self._model: Model                          = None

    def set_model(self, model: Model) -> None:
        self._model = model

    def add_project_include(self, typename: str, include: str) -> None:
        self._project_include_map[typename] = include

    def parse_yaml(self, yaml_text: str) -> None:
        data = yaml.safe_load(yaml_text)

        self._model.set_description(data.get("description", "Model description"))

        self._parse_inheritances(data.get("inherits", []))
        self._parse_members(data.get("members", []))
        self._parse_methods(data.get("methods", []))
        self._parse_constructors(data.get("constructors", []))
        self._parse_evalues(data.get("evalues", []))

    def _parse_inheritances(self, inheritances: list[dict[str, Any]]) -> None:
        for i in inheritances:
            inheritance = Inheritance(i.get("base", "void"), Visibility(i.get("visibility", "public")), i.get("virtual", False))
            self._model.add_inheritance(inheritance)
            self._check_includes(i.get("base", "void"))

    def _parse_members(self, members_data: list[dict[str, Any]]) -> None:
        for m in members_data:
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

    def _parse_methods(self, methods_data: list[dict[str, Any]]) -> None:
        for m in methods_data:
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

    def _parse_constructors(self, constructors_data: list[dict[str, Any]]) -> None:
        for c in constructors_data:
            method = Method("Ignored", c.get("description", "Constructor description"))

            # return type
            mret_type_data = c.get("type", {})
            mret_type = ParameterType(mret_type_data.get("name", ""))
            for st in mret_type_data.get("stereotypes", []):
                mret_type.add_stereotype(Stereotype(st))
            method.set_type(mret_type)

            # parameters
            for p in c.get("params", []):
                param = Parameter(p.get("name", "_defaultParam"), p.get("description", "Parameter description"))

                # type
                ptype_data = p.get("type", {})
                ptype = ParameterType(ptype_data.get("name", "void"))
                for st in ptype_data.get("stereotypes", []):
                    ptype.add_stereotype(Stereotype(st))
                param.set_type(ptype)
                self._check_includes(ptype_data.get("name", "void"))

                method.add_parameter(param)

            self._model.add_constructor(method)

    def _parse_evalues(self, evalues_data: list[dict[str, Any]]) -> None:
        for e in evalues_data:
            evalue = EnumValue(e.get("name", "void"), e.get("value", ""))

            self._model.add_enum_value(evalue)

    def _check_includes(self, typedef: str) -> None:
        if (typedef in self._standard_include_map):
            self._model.add_system_include_h(self._standard_include_map[typedef])
        elif (typedef in self._project_include_map):
            self._model.add_project_include_h(self._project_include_map[typedef])
        else:
            pass
