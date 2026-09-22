from enum import Enum, Flag, auto


__all__ = [
    "ApplicationState",
    "DisplayItemType"
]


class ApplicationState(Enum):
    INIT = auto()
    OPEN = auto()
    BUSY = auto()
# ApplicationState


class DisplayItemType(Flag):
    # the order matters in appending tree items
    FOLDER      = auto()

    ENUM        = auto()
    INTERFACE   = auto()
    CLASS       = auto()

    INHERITANCE = auto()
    MEMBER      = auto()
    METHOD      = auto()

    PARAMETER   = auto()
# DisplayItemType
