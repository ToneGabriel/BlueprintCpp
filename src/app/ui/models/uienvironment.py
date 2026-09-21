from app.ui.interfaces import IQtRoot
from app.ui.generated import (Ui_MainWindow, Ui_CloseProjectDialog, Ui_NewProjectDialog, Ui_HelpDialog)
from app.ui.common import (TreeUIPacket, TableUIPacket, LoggerUIPacket, MenubarUIPacket,
                           HelpDialogUIPacket, NewProjectDialogUIPacket, CloseProjectDialogUIPacket)

from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QStyle)


class UiEnvironment(IQtRoot):
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

        # initialization
        self._app_font.setPointSize(14)
        self._app.setFont(self._app_font)

        self._main_window_widgets.horizontalSplitter.setStretchFactor(0, 1) # tree
        self._main_window_widgets.horizontalSplitter.setStretchFactor(1, 3) # editor

        self._main_window_widgets.verticalSplitter.setStretchFactor(0, 3)   # horizontal splitter (tree + editor)
        self._main_window_widgets.verticalSplitter.setStretchFactor(1, 1)   # logger
    # __init__


    # ===========================================================================
    # Getters
    # ===========================================================================
    def get_tree_uipacket(self) -> TreeUIPacket:
        return TreeUIPacket(tree=self._main_window_widgets.projectTree)
    # get_tree_uipacket


    def get_table_uipacket(self) -> TableUIPacket:
        return TableUIPacket(table=self._main_window_widgets.propertiesTable)
    # get_table_uipacket


    def get_logger_uipacket(self) -> LoggerUIPacket:
        return LoggerUIPacket(logger=self._main_window_widgets.loggTextWindow)
    # get_logger_uipacket


    def get_menubar_uipacket(self) -> MenubarUIPacket:
        return MenubarUIPacket(menubar=self._main_window_widgets.menubar,
                               actionNew=self._main_window_widgets.actionNew,
                               actionOpen=self._main_window_widgets.actionOpen,
                               actionSave=self._main_window_widgets.actionSave,
                               actionClose=self._main_window_widgets.actionClose,
                               actionQuit=self._main_window_widgets.actionQuit,
                               actionGenerate=self._main_window_widgets.actionGenerate,
                               actionAbout=self._main_window_widgets.actionAbout
                               )
    # get_menubar_uipacket


    def get_new_project_dialog_uipacket(self) -> NewProjectDialogUIPacket:
        return NewProjectDialogUIPacket(dialog=self._new_project_dialog,
                                        browseButton=self._new_project_dialog_widgets.browseButton,
                                        projectNameText=self._new_project_dialog_widgets.projectNameText,
                                        projectSavePathText=self._new_project_dialog_widgets.projectSavePathText
                                        )
    # get_new_project_dialog_uipacket


    def get_close_project_dialog_uipacket(self) -> CloseProjectDialogUIPacket:
        return CloseProjectDialogUIPacket(dialog=self._close_project_dialog)
    # get_close_project_dialog_uipacket


    def get_help_dialog_uipacket(self) -> HelpDialogUIPacket:
        return HelpDialogUIPacket(dialog=self._help_dialog)
    # get_help_dialog_uipacket


    # ===========================================================================
    # IQtRoot functionality
    # ===========================================================================
    def run(self) -> None:
        self._main_window.resize(1200, 800)
        self._main_window.showMaximized()
        self._app.exec()
    # run


    def quit(self) -> None:
        self._app.quit()
    # quit

# UiEnvironment
