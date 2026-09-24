from abc import abstractmethod
from typing import Any

from .iloggermanager import ILoggerManager


class ITableManager(ILoggerManager):
    @abstractmethod
    def get_namespaces(self) -> list[str]:...

# ITableManager
