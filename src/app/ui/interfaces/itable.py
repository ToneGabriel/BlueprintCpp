from abc import abstractmethod

from .istate import IState
from app.ui.common import DisplayItemData


class ITable(IState):

    @abstractmethod
    def get_contents(self) -> DisplayItemData:...

    @abstractmethod
    def display_contents(self, dataToDisplay: DisplayItemData) -> None:...

    @abstractmethod
    def clear(self) -> None:...

# ITable
