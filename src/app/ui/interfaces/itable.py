from abc import abstractmethod
from typing import Any

from .istate import IState
from app.ui.common import DisplayItemType


class ITable(IState):

    @abstractmethod
    def get_contents(self) -> dict[str, Any]:...

    @abstractmethod
    def display_contents(self, display: DisplayItemType, data: dict[str, Any]) -> None:...

    @abstractmethod
    def clear(self) -> None:...

