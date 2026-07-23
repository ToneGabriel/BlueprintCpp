from typing import Any
from enum import Enum


# ==============================================================================
class Visibility(Enum):
    PUBLIC      = "public"
    PROTECTED   = "protected"
    PRIVATE     = "private"


# ==============================================================================
class Parameter:
    def __init__(self,
                 name: str = "_defaultMember",
                 description: str = "Parameter description",
                 type: str = "void",
                 indirection: str = None,
                 const: bool = False,
                 volatile: bool = False,
                 default: str = ""
                 ):

        self._param: dict[str, Any] =   {
                                            "name": name,
                                            "description": description,
                                            "type": type,
                                            "indirection": indirection,
                                            "const": const,
                                            "volatile": volatile,
                                            "default": default
                                        }

    @property
    def value(self) -> dict[str, Any]:
        return self._param


# ==============================================================================
class Method:
    def __init__(self,
                 name: str = "_DefaultMethod",
                 description: str = "Method description",
                 type: str = "void",
                 indirection: str = None,
                 const: bool = False,
                 volatile: bool = False,
                 immutable: bool = False,
                 noexcept: bool = False,
                 override: bool = False,
                 ):

        self._method: dict[str, Any] = {
                                            "name": name,
                                            "description": description,
                                            "type": type,
                                            "indirection": indirection,
                                            "const": const,
                                            "volatile": volatile,
                                            "immutable": immutable,
                                            "noexcept": noexcept,
                                            "override": override,
                                            "params": []
                                        }

    @property
    def value(self) -> dict[str, Any]:
        return self._method

    def add_parameter(self, param: Parameter) -> None:
        self._method["params"].append(param.value)


# ==============================================================================
class Inheritance:
    def __init__(self,
                 name: str,
                 visibility: Visibility,
                 virtual: bool
                 ):
        
        self._inheritance: dict[str, Any] = {
                                                "name": name,
                                                "visibility": visibility.value,
                                                "virtual": virtual
                                            }
        
    @property
    def value(self) -> dict[str, Any]:
        return self._inheritance


# ==============================================================================
class EnumValue:
    def __init__(self,
                 name: str,
                 value: str
                 ):
        self._evalue: dict[str, Any] =  {
                                            "name": name,
                                            "value": value
                                        }

    @property
    def value(self) -> dict[str, Any]:
        return self._evalue


# ==============================================================================
class Model:
    def __init__(self, name: str, namespaces: list[str], include_guard: str):

        self._model: dict[str, Any] =   {
                                            "name": name,
                                            "namespaces": namespaces,
                                            "include_guard": include_guard,
                                            "description": "",
                                            "includes_h":   {
                                                                "system": set(),
                                                                "project": set(),
                                                            },
                                            "includes_cpp": set(),
                                            "inherits": [],
                                            "constructors": [],
                                            "members": {
                                                            Visibility.PUBLIC.value: [],
                                                            Visibility.PROTECTED.value: [],
                                                            Visibility.PRIVATE.value: []
                                                        },
                                            "methods": {
                                                            Visibility.PUBLIC.value: [],
                                                            Visibility.PROTECTED.value: [],
                                                            Visibility.PRIVATE.value: []
                                                        },
                                            "evalues": []
                                        }

    @property
    def value(self) -> dict[str, Any]:
        return self._model

    def set_description(self, description: str) -> None:
        self._model["description"] = description

    def add_inheritance(self, inheritance: Inheritance) -> None:
        self._model["inherits"].append(inheritance.value)

    def add_system_include_h(self, include_h: str) -> None:
        self._model["includes_h"]["system"].add(include_h)

    def add_project_include_h(self, include_h: str) -> None:
        self._model["includes_h"]["project"].add(include_h)

    def add_member(self,
                   visibility: Visibility,
                   member: Parameter) -> None:
        self._model["members"][visibility.value].append(member.value)

    def add_method(self,
                   visibility: Visibility,
                   method: Method) -> None:
        self._model["methods"][visibility.value].append(method.value)

    def add_enum_value(self,
                       evalue: EnumValue) -> None:
        self._model["evalues"].append(evalue.value)

    def add_constructor(self,
                        method: Method) -> None:
        self._model["constructors"].append(method.value)
