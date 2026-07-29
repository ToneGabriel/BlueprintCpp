from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTreeView,
    QTextEdit,
    QSplitter,
    QWidget,
    QHBoxLayout
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
        self._window: QMainWindow = None

        # Data
        self._tree_model: QStandardItemModel = None
        self._tree_project_holder: QStandardItem = None

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

        self._tree_project_holder = QStandardItem(project_name)
        self._tree_project_holder.setEditable(False)

        self._tree_model.invisibleRootItem().appendRow(self._tree_project_holder)

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
        self._window.resize(1200, 800)

    def set_busy(self, busy: bool):
        self._work_area.setEnabled(not busy)

    def log(self, message: str):
        self._logger.append(message)

    def start(self):
        self._window.showMaximized()
        self._app.exec()


def main():
    app = GUIApplication()
    app.start()

    # app = QApplication([])
    # window = QMainWindow()

    # # Left widget
    # tree = QTreeView()
    # model = QStandardItemModel()
    # root = model.invisibleRootItem()

    # # model.setHorizontalHeaderLabels(["Project"])
    # tree.setHeaderHidden(True)
    # tree.setModel(model)

    # project = QStandardItem("Project")
    # sub1 = QStandardItem("Sub1")
    # sub2 = QStandardItem("Sub2")
    # class1 = QStandardItem("Class1")
    # class2 = QStandardItem("Class2")
    # class3 = QStandardItem("Class3")

    # root.appendRow(project)
    # tree.expand(project.index())
    # project.setEditable(False)

    # project.appendRow(sub1)
    # project.appendRow(sub2)
    # sub1.appendRow(class1)
    # sub1.appendRow(class2)
    # sub2.appendRow(class3)

    # # Right widget (placeholder)
    # editor = QTextEdit()

    # # Splitter
    # vsplitter = QSplitter(Qt.Horizontal)
    # vsplitter.addWidget(tree)
    # vsplitter.addWidget(editor)

    # # 1/3 : 2/3
    # vsplitter.setSizes([400, 800])

    # window.setCentralWidget(vsplitter)

    # font = QFont()
    # font.setPointSize(14)
    # app.setFont(font)

    # window.resize(1200, 800)
    # window.showMaximized()
    # app.exec()


if __name__ == "__main__":
    main()