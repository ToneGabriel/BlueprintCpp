from enum import Enum, Flag, auto
from dataclasses import dataclass
from typing import Any


__all__ = [
    "ApplicationState",
    "DisplayItemType",
    "DisplayItemData"
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


@dataclass
class DisplayItemData:
    name: str
    prefix: str
    updateTreeDisplay: bool
    itemType: DisplayItemType
    data: dict[str, Any]
# DisplayItemData
