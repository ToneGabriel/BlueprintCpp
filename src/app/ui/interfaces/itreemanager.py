from abc import abstractmethod

from .iloggermanager import ILoggerManager
from app.ui.common import DisplayItemData


class ITreeManager(ILoggerManager):

    @abstractmethod
    def display_table_contents(self, dataToDisplay: DisplayItemData) -> None:...

    @abstractmethod
    def get_table_contents(self) -> DisplayItemData:...

    @abstractmethod
    def store_namespace(self, namespace: str) -> None:...

    @abstractmethod
    def remove_namespace(self, namespace: str) -> None:...

# ITreeManager
