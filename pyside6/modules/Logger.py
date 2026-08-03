import pyside6.interfaces as interfaces

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTreeView,
    QTextEdit,
    QSplitter,
    QWidget,
    QHBoxLayout,
    QStackedWidget
)

from PySide6.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QFont,
)


class Logger(interfaces.ILoggerModule):
    def __init__(self):
        # widgets
        self._q_text = QTextEdit()

        # initialization
        self._q_text.setReadOnly(True)

    def get_root_widget(self) -> QWidget:
        return self._q_text

    def log_message(self, message: str) -> None:
        self._q_text.append(message)

