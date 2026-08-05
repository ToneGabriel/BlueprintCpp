import app.ui.interfaces as interfaces

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


class Editor(interfaces.IEditorModule):
    def __init__(self):
        self._q_text = QTextEdit()

    def get_root_widget(self) -> QWidget:
        return self._q_text
