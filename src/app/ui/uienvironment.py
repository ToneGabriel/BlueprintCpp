import app.ui.generated.ui_mainwindow as mainwindow
import app.ui.generated.ui_newprojectdialog as newprojectdialog
import app.ui.generated.ui_closeprojectdialog as closeprojectdialog
import app.ui.generated.ui_helpdialog as helpdialog

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QStyle,
    QTreeWidgetItem, QTableWidgetItem, QFileDialog,
    QMenu, QTextEdit, QLineEdit, QComboBox, QTableWidget, QTreeWidget)
from PySide6.QtGui import (QFont, QKeySequence)


class UiEnvironment:
    def __init__(self):
        # main widgets
        self._app = QApplication([])
        self._app_font = QFont()
        self._main_window = QMainWindow()
        self._new_project_dialog = QDialog(self._main_window)
        self._close_project_dialog = QDialog(self._main_window)
        self._help_dialog = QDialog(self._main_window)
        self._tree_menu = QMenu(self._main_window)

        # generated widgets
        self._main_window_widgets = mainwindow.Ui_MainWindow()
        self._main_window_widgets.setupUi(self._main_window)

        self._new_project_dialog_widgets = newprojectdialog.Ui_NewProjectDialog()
        self._new_project_dialog_widgets.setupUi(self._new_project_dialog)

        self._close_project_dialog_widgets = closeprojectdialog.Ui_CloseProjectDialog()
        self._close_project_dialog_widgets.setupUi(self._close_project_dialog)

        self._help_dialog_widgets = helpdialog.Ui_HelpDialog()
        self._help_dialog_widgets.setupUi(self._help_dialog)
    # __init__


    def get_menubar_widget(self) -> QMenuBar:
        # TODO: implement
        pass
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


