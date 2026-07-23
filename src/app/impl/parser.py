from app.impl.model import Visibility, Inheritance, Parameter, Method, EnumValue, Model
import yaml
from typing import Any


class Parser:
    def __init__(self,
                 standard_include_map: dict[str, str]
                 ):

        self._standard_include_map: dict[str, str]  = standard_include_map
        self._project_include_map: dict[str, str]   = {}

    def add_project_include(self, typename: str, include: str) -> None:
        self._project_include_map[typename] = include

    def parse_yaml(self, model: Model, yaml_text: str) -> None:
        data = yaml.safe_load(yaml_text) or {}

        self._parse_description(model, data.get("description", "Model description"))
        self._parse_inheritances(model, data.get("inherits", []))
        self._parse_members(model, data.get("members", []))
        self._parse_methods(model, data.get("methods", []))
        self._parse_constructors(model, data.get("constructors", []))
        self._parse_evalues(model, data.get("evalues", []))

    def _parse_description(self, model: Model, description: str) -> None:
        model.set_description(description)

    def _parse_inheritances(self, model: Model, inheritances: list[dict[str, Any]]) -> None:
        for i in inheritances:
            inheritance = Inheritance(i.get("type", "void"), Visibility(i.get("visibility", "public")), i.get("virtual", False))
            model.add_inheritance(inheritance)
            self._add_includes(model, i.get("type", "void"))

    def _parse_members(self, model: Model, members_data: list[dict[str, Any]]) -> None:
        for m in members_data:
            visibility = Visibility(m.get("visibility", "private"))
            member = Parameter(m.get("name", "_defaultMember"),
                               m.get("description", "Member description"),
                               m.get("type", "void"),
                               m.get("indirection", ""),
                               m.get("const", False),
                               m.get("volatile", False),
                               m.get("default", ""),
                               )

            self._add_includes(model, m.get("type", "void"))
            model.add_member(visibility, member)

    def _parse_methods(self, model: Model, methods_data: list[dict[str, Any]]) -> None:
        for m in methods_data:
            visibility = Visibility(m.get("visibility", "public"))
            method = Method(m.get("name", "_DefaultMethod"),
                            m.get("description", "Method description"),
                            m.get("type", "void"),
                            m.get("indirection", ""),
                            m.get("const", False),
                            m.get("volatile", False),
                            m.get("immutable", False),
                            m.get("noexcept", False),
                            m.get("override", False)
                            )

            self._add_includes(model, m.get("type", "void"))

            # parameters
            for p in m.get("params", []):
                param = Parameter(p.get("name", "_defaultParam"),
                                  p.get("description", "Parameter description"),
                                  p.get("type", "void"),
                                  p.get("indirection", ""),
                                  p.get("const", False),
                                  p.get("volatile", False),
                                  p.get("default", ""),
                                  )

                self._add_includes(model, p.get("type", "void"))
                method.add_parameter(param)

            model.add_method(visibility, method)

    def _parse_constructors(self, model: Model, constructors_data: list[dict[str, Any]]) -> None:
        for c in constructors_data:
            method = Method("Ignored", c.get("description", "Constructor description"))

            # parameters
            for p in c.get("params", []):
                param = Parameter(p.get("name", "_defaultParam"),
                                  p.get("description", "Parameter description"),
                                  p.get("type", "void"),
                                  p.get("indirection", ""),
                                  p.get("const", False),
                                  p.get("volatile", False),
                                  p.get("default", ""),
                                  )

                self._add_includes(model, p.get("type", "void"))
                method.add_parameter(param)

            model.add_constructor(method)

    def _parse_evalues(self, model: Model, evalues_data: list[dict[str, Any]]) -> None:
        for e in evalues_data:
            evalue = EnumValue(e.get("name", "void"), e.get("value", ""))

            model.add_enum_value(evalue)

    def _add_includes(self, model: Model, typedef: str) -> None:
        std_types: list[str] = self._extract_std_types(typedef)

        for t in std_types:
            if (t in self._standard_include_map):
                model.add_system_include_h(self._standard_include_map[t])

        if (typedef in self._project_include_map):
            model.add_project_include_h(self._project_include_map[typedef])
    
    def _extract_std_types(self, typedef: str) -> list[str]:
        results = []
        i = 0
        n = len(typedef)

        while i < n:
            if typedef.startswith("std::", i):
                start = i
                i += 5  # skip "std::"

                # Read full identifier (including nested namespaces)
                while i < n and (typedef[i].isalnum() or typedef[i] in "_:"):
                    i += 1

                results.append(typedef[start:i])
            else:
                i += 1

        return results
