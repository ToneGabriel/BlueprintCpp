from abc import abstractmethod

from .iloggermanager import ILoggerManager


class IMenuManager(ILoggerManager):

    @abstractmethod
    def open_new_project(self) -> None:...

    @abstractmethod
    def open_existing_project(self) -> None:...

    @abstractmethod
    def save_project(self) -> None:...

    @abstractmethod
    def close_project(self) -> None:...

    @abstractmethod
    def quit_application(self) -> None:...

    @abstractmethod
    def generate_code(self) -> None:...
