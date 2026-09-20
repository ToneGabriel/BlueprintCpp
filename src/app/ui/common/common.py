from enum import Enum, Flag, auto


__all__ = [
    "ApplicationState",
    "DisplayItemType",
    "MenubarAction"
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


class MenubarAction(Enum):
    ACTION_NEW      = auto()
    ACTION_OPEN     = auto()
    ACTION_SAVE     = auto()
    ACTION_CLOSE    = auto()
    ACTION_QUIT     = auto()
    ACTION_GENERATE = auto()
    ACTION_ABOUT    = auto()
