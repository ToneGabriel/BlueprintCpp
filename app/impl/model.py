from typing import Any
from enum import Enum


class Stereotype(Enum):
    VIRTUAL         = "virtual"
    VIRTUAL_0       = "virtual_0"
    CONST           = "const"
    IMMUTABLE       = "immutable"
    VOLATILE        = "volatile"
    NOEXCEPT        = "noexcept"
    OVERRIDE        = "override"
    STATIC          = "static"
    ARRAY           = "array"
    POINTER         = "pointer"
    LVAL_REFERENCE  = "lval_reference"
    RVAL_REFERENCE  = "rval_reference"


class Visibility(Enum):
    PUBLIC      = "public"
    PROTECTED   = "protected"
    PRIVATE     = "private"


class ParameterType:
    def __init__(self, name: str):
        self._type: dict[str, Any] =    {
                                            "name": name,
                                            "stereotypes":  {
                                                                s.value: False for s in Stereotype
                                                            }
                                        }
    @property
    def value(self) -> dict[str, Any]:
        return self._type

    def add_stereotype(self, stereotype: Stereotype) -> None:
        self._type["stereotypes"][stereotype.value] = True


class Parameter:
    def __init__(self,
                 name: str,
                 description: str
                 ):

        self._param: dict[str, Any] =   {
                                            "name": name,
                                            "type": {},
                                            "description": description
                                        }

        self.set_type(ParameterType("void"))

    @property
    def value(self) -> dict[str, Any]:
        return self._param
    
    def set_type(self, type: ParameterType) -> None:
        self._param["type"] = type.value


class Method:
    def __init__(self,
                 name: str,
                 description: str
                 ):

        self._method: dict[str, Any] = {
                                            "name": name,
                                            "type": {},
                                            "description": description,
                                            "params": []
                                        }

        self.set_type(ParameterType("void"))

    @property
    def value(self) -> dict[str, Any]:
        return self._method

    def set_type(self, type: ParameterType) -> None:
        self._method["type"] = type.value

    def add_parameter(self, param: Parameter) -> None:
        self._method["params"].append(param.value)


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
                                            "destructor": {},
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
                                                        }
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

