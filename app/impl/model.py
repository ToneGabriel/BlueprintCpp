from typing import Any
from enum import Enum


class ParameterStereotype(Enum):
    CONST           = "const"
    VOLATILE        = "volatile"
    ARRAY           = "array"
    POINTER         = "pointer"
    LVAL_REFERENCE  = "lval_reference"
    RVAL_REFERENCE  = "rval_reference"


class MethodStereotype(Enum):
    VIRTUAL     = "virtual"
    VIRTUAL_0   = "virtual_0"
    CONST       = "const"
    NOEXCEPT    = "noexcept"
    OVERRIDE    = "override"


class Visibility(Enum):
    PUBLIC      = "public"
    PROTECTED   = "protected"
    PRIVATE     = "private"


class ParameterType:
    def __init__(self, name: str):
        self._type: dict[str, Any] =    {
                                            "name": name,
                                            "stereotypes":  {
                                                                s.value: False for s in ParameterStereotype
                                                            }
                                        }
    @property
    def value(self) -> dict[str, Any]:
        return self._type

    def add_stereotype(self, stereotype: ParameterStereotype) -> None:
        self._type["stereotypes"][stereotype.value] = True


class Parameter:
    def __init__(self,
                 name: str,
                 type: str,
                 description: str):

        self._param: dict[str, Any] =   {
                                            "name": name,
                                            "type": type,
                                            "description": description
                                        }

    @property
    def value(self) -> dict[str, Any]:
        return self._param


class Method:
    def __init__(self,
                 name: str,
                 return_type: str,
                 description: str):

        self._method: dict[str, Any] = {
                                            "name": name,
                                            "return_type": return_type,
                                            "description": description,
                                            "params": [],
                                            "stereotypes":  {
                                                                s.value: False for s in MethodStereotype
                                                            }
                                        }

    @property
    def value(self) -> dict[str, Any]:
        return self._method

    def add_parameter(self, param: Parameter) -> None:
        self._method["params"].append(param.value)

    def add_stereotype(self, stereotype: MethodStereotype) -> None:
        self._method["stereotypes"][stereotype.value] = True


class Model:
    def __init__(self,
                 name: str,
                 type: str,
                 description: str,
                 ):

        self._model: dict[str, Any] =   {
                                            "name": name,
                                            "type": type,
                                            "description": description,
                                            "namespaces": [],
                                            "include_guard": "",
                                            "includes": [],
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

    def add_member(self,
                   visibility: Visibility,
                   member: Parameter) -> None:
        self._model["members"][visibility.value].append(member.value)

    def add_method(self,
                   visibility: Visibility,
                   method: Method) -> None:
        self._model["methods"][visibility.value].append(method.value)

