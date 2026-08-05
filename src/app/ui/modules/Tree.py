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
    QStandardItem
)


class Tree(interfaces.ITreeModule):
    def __init__(self, name: str="Project"):
        # external references
        self._editor: interfaces.IEditorModule = None

        # widgets
        self._q_tree = QTreeView()
        self._q_tree_model = QStandardItemModel()
        self._q_tree_project_node = QStandardItem(name)

        # initialization
        self._q_tree.setHeaderHidden(True)
        self._q_tree.setModel(self._q_tree_model)
        self._q_tree_model.invisibleRootItem().appendRow(self._q_tree_project_node)
        self._q_tree_project_node.setEditable(False)

    def get_root_widget(self) -> QWidget:
        return self._q_tree

    def set_editor_reference(self, editor: interfaces.IEditorModule) -> None:
        self._editor = editor

    # def add_node(self, name: str, parent: QStandardItem) -> None:
    #     node = QStandardItem(name)
    #     parent.appendRow(node)


