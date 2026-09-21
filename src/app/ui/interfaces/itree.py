from abc import abstractmethod

from .istate import IState


class ITree(IState):

    @abstractmethod
    def create_root(self, name: str) -> None:...

    @abstractmethod
    def clear(self) -> None:...

# ITree
