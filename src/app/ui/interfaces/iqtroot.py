from abc import ABC, abstractmethod


class IQtRoot(ABC):

    @abstractmethod
    def run(self) -> None:...

    @abstractmethod
    def quit(self) -> None:...

# IQtRoot
