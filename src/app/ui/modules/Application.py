import app.ui.interfaces as interfaces

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QSplitter,
    QWidget,
    QHBoxLayout,
    QStackedWidget
)

from PySide6.QtGui import (
    QFont
)


class Application:
    def __init__(self):
        # external references
        self._tree: interfaces.ITreeModule = None
        self._editor: interfaces.IEditorModule = None
        self._logger: interfaces.ILoggerModule = None

        # widgets
        self._q_app = QApplication([])
        self._q_window = QMainWindow()

        self._q_font = QFont()

        self._q_vertical_splitter = QSplitter(Qt.Horizontal)
        self._q_horizontal_splitter = QSplitter(Qt.Vertical)
        self._q_work_area = QWidget()
        self._q_work_layout = QHBoxLayout(self._q_work_area)

        # initialization
        self._q_font.setPointSize(14)
        self._q_app.setFont(self._q_font)

        self._q_work_layout.setContentsMargins(0, 0, 0, 0)
        self._q_work_layout.addWidget(self._q_vertical_splitter)

        self._q_horizontal_splitter.addWidget(self._q_work_area)

        self._q_window.setCentralWidget(self._q_horizontal_splitter)

    def set_tree_reference(self, tree: interfaces.ITreeModule) -> None:
        if self._tree is not None:
            raise RuntimeError("Tree module already set")

        self._tree = tree
        self._q_vertical_splitter.addWidget(self._tree.get_root_widget())

    def set_editor_reference(self, editor: interfaces.IEditorModule) -> None:
        if self._editor is not None:
            raise RuntimeError("Editor module already set")

        self._editor = editor
        self._q_vertical_splitter.addWidget(self._editor.get_root_widget())

    def set_logger_reference(self, logger: interfaces.ILoggerModule) -> None:
        if self._logger is not None:
            raise RuntimeError("Logger module already set")

        self._logger = logger
        self._q_horizontal_splitter.addWidget(self._logger.get_root_widget())

    def run(self) -> None:
        if self._tree is None:
            raise RuntimeError("Tree module NOT set")

        if self._editor is None:
            raise RuntimeError("Editor module NOT set")

        if self._logger is None:
            raise RuntimeError("Logger module NOT set")

        self._q_vertical_splitter.setSizes([400, 800])
        self._q_horizontal_splitter.setSizes([800, 300])

        self._q_window.resize(1200, 800)
        self._q_window.setWindowTitle("Blueprint::Cpp")
        self._q_window.showMaximized()

        self._q_app.exec()

    def _set_busy(self, busy: bool):
        self._q_work_area.setEnabled(not busy)
