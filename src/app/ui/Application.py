import app.ui.generated.ui_mainwindow as mainwindow
import app.ui.generated.ui_newprojectdialog as newprojectdialog
import app.ui.generated.ui_closeprojectdialog as closeprojectdialog
import app.ui.generated.ui_helpdialog as helpdialog

from enum import Enum
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QStyle, QTreeWidgetItem)
from PySide6.QtGui import (
    QFont, QKeySequence)


class ApplicationState(Enum):
    INIT = 0
    OPEN = 1
    BUSY = 2


class Application:
    def __init__(self):
        # main widgets
        self._app = QApplication([])
        self._app_font = QFont()
        self._main_window = QMainWindow()
        self._new_project_dialog = QDialog(self._main_window)
        self._close_project_dialog = QDialog(self._main_window)
        self._help_dialog = QDialog(self._main_window)

        # generated widgets
        self._main_window_widgets = mainwindow.Ui_MainWindow()
        self._main_window_widgets.setupUi(self._main_window)

        self._new_project_dialog_widgets = newprojectdialog.Ui_NewProjectDialog()
        self._new_project_dialog_widgets.setupUi(self._new_project_dialog)

        self._close_project_dialog_widgets = closeprojectdialog.Ui_CloseProjectDialog()
        self._close_project_dialog_widgets.setupUi(self._close_project_dialog)

        self._help_dialog_widgets = helpdialog.Ui_HelpDialog()
        self._help_dialog_widgets.setupUi(self._help_dialog)

        # initialization
        self._init_font()
        self._init_main_window()
        self._init_menu_bar()

        self._set_application_state(ApplicationState.INIT)
    # __init__


    def run(self) -> None:
        self._main_window.resize(1200, 800)
        self._main_window.showMaximized()
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

        self._main_window_widgets.loggTextWindow.setReadOnly(True)
    # _init_main_window


    def _init_menu_bar(self) -> None:
        self._main_window_widgets.actionNew.triggered.connect(self._open_project_dialog)
        self._main_window_widgets.actionNew.setShortcut(QKeySequence.New)
        self._main_window_widgets.actionNew.setIcon(self._main_window.style().standardIcon(QStyle.SP_FileIcon))

        self._main_window_widgets.actionOpen.triggered.connect(self._open_project_dialog)
        self._main_window_widgets.actionOpen.setShortcut(QKeySequence.Open)
        self._main_window_widgets.actionOpen.setIcon(self._main_window.style().standardIcon(QStyle.SP_DirIcon))

        self._main_window_widgets.actionSave.triggered.connect(self._save_project)
        self._main_window_widgets.actionSave.setShortcut(QKeySequence.Save)
        self._main_window_widgets.actionSave.setIcon(self._main_window.style().standardIcon(QStyle.SP_DialogSaveButton))

        self._main_window_widgets.actionClose.triggered.connect(self._close_project)
        self._main_window_widgets.actionClose.setShortcut(QKeySequence.Close)

        self._main_window_widgets.actionQuit.triggered.connect(self._quit_application)
        self._main_window_widgets.actionQuit.setShortcut(QKeySequence.Quit)
        self._main_window_widgets.actionQuit.setIcon(self._main_window.style().standardIcon(QStyle.SP_DialogCloseButton))

        # TODO: add trigger
        # self._main_window_widgets.actionGenerate.triggered.connect(self.)
        self._main_window_widgets.actionGenerate.setIcon(self._main_window.style().standardIcon(QStyle.SP_MediaPlay))

        self._main_window_widgets.actionAbout.triggered.connect(self._open_help_dialog)
        self._main_window_widgets.actionAbout.setIcon(self._main_window.style().standardIcon(QStyle.SP_TitleBarContextHelpButton))
    # _init_menu_bar


    def _open_project_dialog(self) -> None:
        self._new_project_dialog.exec()
        self._open_new_project()    # TODO: remove from here
    # _open_project_dialog


    def _open_new_project(self) -> None:
        item = QTreeWidgetItem(["Project"])
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        item.setIcon(0, self._main_window.style().standardIcon(QStyle.SP_DirIcon))
        self._main_window_widgets.projectTree.addTopLevelItem(item)

        self._set_application_state(ApplicationState.OPEN)
    # _open_new_project


    def _save_project(self) -> None:
        # TODO: implement
        self._log_message("Project successfully saved!")
    # _save_project


    def _close_project(self) -> None:
        result = self._close_project_dialog.exec()

        if result == QDialog.Accepted:
            self._main_window_widgets.projectTree.clear()

            self._main_window_widgets.propertiesTable.clearContents()
            self._main_window_widgets.propertiesTable.setRowCount(0)

            self._set_application_state(ApplicationState.INIT)
        else:
            # just close the dialog
            pass
    # _close_project


    def _quit_application(self) -> None:
        self._app.quit()
    # _quit_application


    def _open_help_dialog(self) -> None:
        self._help_dialog.exec()
    # _open_help_dialog


    def _set_application_state(self, state: ApplicationState) -> None:
        match state:
            case ApplicationState.INIT:
                self._main_window_widgets.menubar.setEnabled(True)
                self._main_window_widgets.horizontalSplitter.setEnabled(True)   # tree + editor

                self._main_window_widgets.actionNew.setEnabled(True)
                self._main_window_widgets.actionOpen.setEnabled(True)

                self._main_window_widgets.actionSave.setEnabled(False)
                self._main_window_widgets.actionClose.setEnabled(False)
                self._main_window_widgets.actionGenerate.setEnabled(False)

            case ApplicationState.OPEN:
                self._main_window_widgets.menubar.setEnabled(True)
                self._main_window_widgets.horizontalSplitter.setEnabled(True)   # tree + editor

                self._main_window_widgets.actionNew.setEnabled(False)
                self._main_window_widgets.actionOpen.setEnabled(False)

                self._main_window_widgets.actionSave.setEnabled(True)
                self._main_window_widgets.actionClose.setEnabled(True)
                self._main_window_widgets.actionGenerate.setEnabled(True)

            case ApplicationState.BUSY:
                self._main_window_widgets.menubar.setEnabled(False)
                self._main_window_widgets.horizontalSplitter.setEnabled(False)  # tree + editor
    # _set_application_state


    def _log_message(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._main_window_widgets.loggTextWindow.append(f"[{timestamp}] - {message}")
    # _log_message
