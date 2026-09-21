from abc import ABC, abstractmethod


class IQuit(ABC):

    @abstractmethod
    def quit(self) -> None:...
