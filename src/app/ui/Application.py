import app.ui.generated.ui_mainwindow as mainwindow
import app.ui.generated.ui_newprojectdialog as newprojectdialog

from enum import Enum

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QStyle)
from PySide6.QtGui import (
    QFont, QKeySequence)


class ApplicationState(Enum):
    INIT = 0
    OPEN = 1
    BUSY = 2


class Application:
    def __init__(self):
        # state
        self._state = ApplicationState.INIT

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
        self._init_menu_bar()
        self._init_logger()

        self._set_init_state()
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

    def _init_menu_bar(self) -> None:
        self._main_window_widgets.actionOpen.triggered.connect(self._open_project_dialog)
        self._main_window_widgets.actionOpen.setShortcut(QKeySequence.Open)
        self._main_window_widgets.actionOpen.setIcon(self._main_window.style().standardIcon(QStyle.SP_FileIcon))

        self._main_window_widgets.actionSave.triggered.connect(self._save_project)
        self._main_window_widgets.actionSave.setShortcut(QKeySequence.Save)
        self._main_window_widgets.actionSave.setIcon(self._main_window.style().standardIcon(QStyle.SP_DialogSaveButton))

        self._main_window_widgets.actionClose.triggered.connect(self._close_project)
        self._main_window_widgets.actionClose.setShortcut(QKeySequence.Close)

        self._main_window_widgets.actionQuit.triggered.connect(self._quit_application)
        self._main_window_widgets.actionQuit.setShortcut(QKeySequence.Quit)
        self._main_window_widgets.actionQuit.setIcon(self._main_window.style().standardIcon(QStyle.SP_DialogCloseButton))

        # self._main_window_widgets.actionGenerate.setShortcut(QKeySequence.)
        # self._main_window_widgets.actionGenerate.triggered.connect(self.)
        self._main_window_widgets.actionGenerate.setIcon(self._main_window.style().standardIcon(QStyle.SP_MediaPlay))
    # _init_menu_bar

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

    def _close_project(self) -> None:
        pass
    # _close_project

    def _quit_application(self) -> None:
        self._app.quit()
    # _quit_application

    def _set_init_state(self) -> None:
        self._state = ApplicationState.INIT

        self._main_window_widgets.menubar.setEnabled(True)
        self._main_window_widgets.horizontalSplitter.setEnabled(True)

        self._main_window_widgets.actionOpen.setEnabled(True)
        self._main_window_widgets.actionSave.setEnabled(False)
        self._main_window_widgets.actionClose.setEnabled(False)
        self._main_window_widgets.actionGenerate.setEnabled(False)
    # _set_init_state

    def _set_open_state(self) -> None:
        self._state = ApplicationState.OPEN

        self._main_window_widgets.menubar.setEnabled(True)
        self._main_window_widgets.horizontalSplitter.setEnabled(True)

        self._main_window_widgets.actionOpen.setEnabled(False)
        self._main_window_widgets.actionSave.setEnabled(True)
        self._main_window_widgets.actionClose.setEnabled(True)
        self._main_window_widgets.actionGenerate.setEnabled(True)
    # _set_open_state

    def _set_busy_state(self) -> None:
        self._state = ApplicationState.BUSY

        self._main_window_widgets.menubar.setEnabled(False)
        self._main_window_widgets.horizontalSplitter.setEnabled(False)
    # _set_busy_state
