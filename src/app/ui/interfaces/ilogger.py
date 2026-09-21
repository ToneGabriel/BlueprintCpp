from abc import abstractmethod

from .istate import IState


class ILogger(IState):

    @abstractmethod
    def log_message(self, message: str) -> None:...

    @abstractmethod
    def clear_logs(self) -> None:...

# ILogger
