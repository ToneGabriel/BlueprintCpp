from app.ui.common import MenubarAction
from app.ui.generated import (Ui_MainWindow, Ui_CloseProjectDialog, Ui_NewProjectDialog, Ui_HelpDialog)

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QStyle, QMenuBar,
    QTreeWidgetItem, QTableWidgetItem, QFileDialog,
    QMenu, QTextEdit, QLineEdit, QComboBox, QTableWidget, QTreeWidget)
from PySide6.QtGui import (QFont, QKeySequence, QAction)


class UiEnvironment:
    def __init__(self):
        # main widgets
        self._app = QApplication([])
        self._app_font = QFont()
        self._main_window = QMainWindow()
        self._new_project_dialog = QDialog(self._main_window)
        self._close_project_dialog = QDialog(self._main_window)
        self._help_dialog = QDialog(self._main_window)

        # generated widgets
        self._main_window_widgets = Ui_MainWindow()
        self._main_window_widgets.setupUi(self._main_window)

        self._new_project_dialog_widgets = Ui_NewProjectDialog()
        self._new_project_dialog_widgets.setupUi(self._new_project_dialog)

        self._close_project_dialog_widgets = Ui_CloseProjectDialog()
        self._close_project_dialog_widgets.setupUi(self._close_project_dialog)

        self._help_dialog_widgets = Ui_HelpDialog()
        self._help_dialog_widgets.setupUi(self._help_dialog)
    # __init__


    def get_menubar_action_widgets(self) -> dict[MenubarAction, QAction]:
        actions = {
            MenubarAction.ACTION_NEW:       self._main_window_widgets.actionNew,
            MenubarAction.ACTION_OPEN:      self._main_window_widgets.actionOpen,
            MenubarAction.ACTION_SAVE:      self._main_window_widgets.actionSave,
            MenubarAction.ACTION_CLOSE:     self._main_window_widgets.actionClose,
            MenubarAction.ACTION_QUIT:      self._main_window_widgets.actionQuit,
            MenubarAction.ACTION_GENERATE:  self._main_window_widgets.actionGenerate,
            MenubarAction.ACTION_ABOUT:     self._main_window_widgets.actionAbout
        }

        return actions
    # get_menubar_action_widgets


    def get_menubar_widget(self) -> QMenuBar:
        return self._main_window_widgets.menubar
    # get_menubar_widget


    def get_logger_widget(self) -> QTextEdit:
        return self._main_window_widgets.loggTextWindow
    # get_logger_widget


    def get_tree_widget(self) -> QTreeWidget:
        return self._main_window_widgets.projectTree
    # get_tree_widget


    def get_table_widget(self) -> QTableWidget:
        return self._main_window_widgets.propertiesTable
    # get_table_widget


    def run(self) -> None:
        self._main_window.resize(1200, 800)
        self._main_window.showMaximized()
        self._app.exec()
    # run


    def quit(self) -> None:
        self._app.quit()
    # quit
