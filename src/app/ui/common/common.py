from enum import Enum, Flag, auto


__all__ = [
    "ApplicationState",
    "DisplayItemType"
]


class ApplicationState(Enum):
    INIT = auto()
    OPEN = auto()
    BUSY = auto()


class DisplayItemType(Flag):
    FOLDER      = auto()
    CLASS       = auto()
    INTERFACE   = auto()
    ENUM        = auto()
    INHERITANCE = auto()
    MEMBER      = auto()
    METHOD      = auto()
    PARAMETER   = auto()

