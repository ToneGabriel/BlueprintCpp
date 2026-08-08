import app.ui.generated.ui_mainwindow as mainwindow

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)

from PySide6.QtGui import (
    QFont
)


class Application:
    def __init__(self):
        # main widgets
        self._app = QApplication([])
        self._main_window = QMainWindow()
        self._app_font = QFont()

        # generated widgets
        self._main_window_widgets = mainwindow.Ui_MainWindow()
        self._main_window_widgets.setupUi(self._main_window)

        # initialization
        self._init_font()
        self._init_main_window()
        self._init_logger()

    def run(self) -> None:
        # app = QApplication([])

        # self._main_window = QMainWindow()
        # self._main_window_widgets.setupUi(self._main_window)

        # self._q_vertical_splitter.setSizes([400, 800])
        # self._q_horizontal_splitter.setSizes([800, 300])

        # self._main_window.setWindowFlags(
        #     Qt.Window |
        #     Qt.CustomizeWindowHint |
        #     Qt.WindowTitleHint |
        #     Qt.WindowCloseButtonHint)

        self._main_window.resize(1200, 800)
        self._main_window.showMaximized()

        self._app.exec()

    def _init_font(self) -> None:
        self._app_font.setPointSize(14)
        self._app.setFont(self._app_font)

    def _init_main_window(self) -> None:
        self._main_window_widgets.horizontalSplitter.setStretchFactor(0, 1) # tree
        self._main_window_widgets.horizontalSplitter.setStretchFactor(1, 3) # editor

        self._main_window_widgets.verticalSplitter.setStretchFactor(0, 3)   # horizontal splitter (tree + editor)
        self._main_window_widgets.verticalSplitter.setStretchFactor(1, 1)   # logger

    def _init_logger(self) -> None:
        self._main_window_widgets.loggTextWindow.setReadOnly(True)

    def _log_message(self, message: str) -> None:
        self._main_window_widgets.loggTextWindow.append(message)

    # def _set_busy(self, busy: bool):
    #     self._q_work_area.setEnabled(not busy)
