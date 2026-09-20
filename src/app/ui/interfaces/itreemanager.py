from abc import abstractmethod
from typing import Any

from .iloggermanager import ILoggerManager
from app.ui.common import DisplayItemType


class ITreeManager(ILoggerManager):

    @abstractmethod
    def display_table_contents(self, display: DisplayItemType, data: dict[str, Any]) -> None:...

    @abstractmethod
    def get_table_contents(self) -> dict[str, Any]:...



