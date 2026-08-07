import app.ui.generated.ui_mainwindow as mainwindow

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
        # widgets
        self._q_window = QMainWindow()

        self._window_widgets = mainwindow.Ui_MainWindow()

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

    def run(self) -> None:
        app = QApplication([])

        self._main_window = QMainWindow()
        self._window_widgets.setupUi(self._main_window)

        self._q_vertical_splitter.setSizes([400, 800])
        self._q_horizontal_splitter.setSizes([800, 300])

        self._main_window.resize(1200, 800)
        self._main_window.showMaximized()

        app.exec()

    def _set_busy(self, busy: bool):
        self._q_work_area.setEnabled(not busy)
