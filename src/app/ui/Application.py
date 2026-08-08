import app.ui.generated.ui_mainwindow as mainwindow
import app.ui.generated.ui_newprojectdialog as newprojectdialog

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog
)

from PySide6.QtGui import (
    QFont
)


class Application:
    def __init__(self):
        # main widgets
        self._app = QApplication([])
        self._app_font = QFont()
        self._main_window = QMainWindow()
        self._new_project_dialog = QDialog(self._main_window)

        # generated widgets
        self._main_window_widgets = mainwindow.Ui_MainWindow()
        self._main_window_widgets.setupUi(self._main_window)

        self._new_project_dialog_widgets = newprojectdialog.Ui_NewProjectDialog()
        self._new_project_dialog_widgets.setupUi(self._new_project_dialog)

        # initialization
        self._init_font()
        self._init_main_window()
        self._init_logger()
    # __init__

    def run(self) -> None:
        # self._main_window.setWindowFlags(
        #     Qt.Window |
        #     Qt.CustomizeWindowHint |
        #     Qt.WindowTitleHint |
        #     Qt.WindowCloseButtonHint)

        self._main_window.resize(1200, 800)
        self._main_window.showMaximized()

        self._new_project_dialog.exec()

        self._app.exec()
    # run

    def _init_font(self) -> None:
        self._app_font.setPointSize(14)
        self._app.setFont(self._app_font)
    # _init_font

    def _init_main_window(self) -> None:
        self._main_window_widgets.horizontalSplitter.setStretchFactor(0, 1) # tree
        self._main_window_widgets.horizontalSplitter.setStretchFactor(1, 3) # editor

        self._main_window_widgets.verticalSplitter.setStretchFactor(0, 3)   # horizontal splitter (tree + editor)
        self._main_window_widgets.verticalSplitter.setStretchFactor(1, 1)   # logger
    # _init_main_window

    def _init_logger(self) -> None:
        self._main_window_widgets.loggTextWindow.setReadOnly(True)
    # _init_logger

    def _log_message(self, message: str) -> None:
        self._main_window_widgets.loggTextWindow.append(message)
    # _log_message

    def _open_project_dialog(self) -> None:
        self._new_project_dialog.exec()
    # _open_project_dialog

    def _save_project(self) -> None:
        pass
    # _save_project

    def _quit_application(self) -> None:
        self._app.quit()
    # _quit_application

    def _set_busy(self, busy: bool) -> None:
        self._main_window_widgets.menubar.setEnabled(not busy)
        self._main_window_widgets.horizontalSplitter.setEnabled(not busy)
    # _set_busy
