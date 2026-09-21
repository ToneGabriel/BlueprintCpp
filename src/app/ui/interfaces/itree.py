from abc import abstractmethod

from .istate import IState


class ITree(IState):

    @abstractmethod
    def clear(self) -> None:...
