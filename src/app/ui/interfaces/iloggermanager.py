from abc import ABC, abstractmethod


class ILoggerManager(ABC):

    @abstractmethod
    def log_message(self, message: str) -> None:...

# ILoggerManager
