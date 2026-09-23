from abc import abstractmethod

from .iloggermanager import ILoggerManager
from app.ui.common import DisplayItemData


class ITreeManager(ILoggerManager):

    @abstractmethod
    def display_table_contents(self, dataToDisplay: DisplayItemData) -> None:...

    @abstractmethod
    def get_table_contents(self) -> DisplayItemData:...

# ITreeManager
