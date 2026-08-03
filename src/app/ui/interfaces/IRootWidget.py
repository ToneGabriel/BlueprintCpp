from abc import ABC, abstractmethod

from PySide6.QtWidgets import (
    QWidget
)

class IRootWidget(ABC):

    @abstractmethod
    def get_root_widget(self) -> QWidget:
        pass

