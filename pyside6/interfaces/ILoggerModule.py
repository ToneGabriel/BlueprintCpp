from abc import ABC, abstractmethod
from .IRootWidget import IRootWidget


class IloggerModule(IRootWidget):

    @abstractmethod
    def log_message(self, message: str) -> None:
        pass
