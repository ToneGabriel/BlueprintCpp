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

class GUIApplication:
    def __init__(self):
        # Application
        self._app: QApplication = None

        # Main window
        self._window: QMainWindow = None

        # Stack that holds all pages
        # self._stack: QStackedWidget = None

        # Page to start a project from
        self._project_manager_page: QWidget = None

        # Page to edit the project after it's selected
        self._project_editor_page: QWidget = None

        # Data
        self._tree_model: QStandardItemModel = None
        self._tree_project_node: QStandardItem = None

        # Widgets
        self._tree: QTreeView = None
        self._editor: QTextEdit = None
        self._logger: QTextEdit = None

        # Containers
        self._work_area: QWidget = None
        self._vertical_splitter: QSplitter = None
        self._horizontal_splitter: QSplitter = None

        self._init_app()
        self._init_tree("Project")
        self._init_editor()
        self._init_logger()
        self._init_window()

    def _init_app(self):
        self._app = QApplication([])

        font = QFont()
        font.setPointSize(14)
        self._app.setFont(font)

    def _init_tree(self, project_name: str):
        self._tree_model = QStandardItemModel()

        self._tree = QTreeView()
        self._tree.setHeaderHidden(True)
        self._tree.setModel(self._tree_model)

        self._tree_project_node = QStandardItem(project_name)
        self._tree_project_node.setEditable(False)

        # sub1 = QStandardItem("Sub1")
        # sub2 = QStandardItem("Sub2")
        # class1 = QStandardItem("Class1")
        # class2 = QStandardItem("Class2")
        # class3 = QStandardItem("Class3")

        # self._tree_project_node.appendRow(sub1)
        # self._tree_project_node.appendRow(sub2)
        # sub1.appendRow(class1)
        # sub1.appendRow(class2)
        # sub2.appendRow(class3)

        self._tree_model.invisibleRootItem().appendRow(self._tree_project_node)

    def _init_editor(self):
        self._editor = QTextEdit()

    def _init_logger(self):
        self._logger = QTextEdit()
        self._logger.setReadOnly(True)

    def _init_window(self):
        self._window = QMainWindow()

        # Work area (tree + editor)
        self._vertical_splitter = QSplitter(Qt.Horizontal)
        self._vertical_splitter.addWidget(self._tree)
        self._vertical_splitter.addWidget(self._editor)
        self._vertical_splitter.setSizes([400, 800])

        self._work_area = QWidget()

        work_layout = QHBoxLayout(self._work_area)
        work_layout.setContentsMargins(0, 0, 0, 0)
        work_layout.addWidget(self._vertical_splitter)

        # Main splitter
        self._horizontal_splitter = QSplitter(Qt.Vertical)
        self._horizontal_splitter.addWidget(self._work_area)
        self._horizontal_splitter.addWidget(self._logger)
        self._horizontal_splitter.setSizes([800, 300])

        self._window.setCentralWidget(self._horizontal_splitter)
        self._window.setWindowTitle("Blueprint::Cpp")
        self._window.resize(1200, 800)

    def set_busy(self, busy: bool):
        self._work_area.setEnabled(not busy)

    def log(self, message: str):
        self._logger.append(message)

    def start(self):
        self._window.showMaximized()
        self._app.exec()


# class GUITree:
#     def __init__(self, name: str):
#         self._tree = QTreeView()
#         self._tree_model = QStandardItemModel()
#         self._tree_project_node = QStandardItem(name)

#         self._tree.setHeaderHidden(True)
#         self._tree.setModel(self._tree_model)
#         self._tree_model.invisibleRootItem().appendRow(self._tree_project_node)
#         self._tree_project_node.setEditable(False)

#     def add_node(self, name: str, parent: QStandardItem) -> None:
#         node = QStandardItem(name)
#         parent.appendRow(node)


def main():
    app = GUIApplication()
    app.start()


if __name__ == "__main__":
    main()

