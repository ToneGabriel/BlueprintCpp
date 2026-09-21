from abc import abstractmethod

from .iloggermanager import ILoggerManager


class IMenuManager(ILoggerManager):

    @abstractmethod
    def open_new_project(self, name: str, path: str) -> None:...

    @abstractmethod
    def open_existing_project(self, path: str) -> None:...

    @abstractmethod
    def save_project(self) -> None:...

    @abstractmethod
    def close_project(self) -> None:...

    @abstractmethod
    def quit_application(self) -> None:...

    @abstractmethod
    def generate_project_files(self) -> None:...
