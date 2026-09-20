from PySide6.QtWidgets import QTextEdit, QMenuBar, QStyle
from PySide6.QtGui import QAction, QKeySequence

from app.ui.common import ApplicationState, MenubarAction
from app.ui.interfaces import IMenu, IMenuManager


class MenuWrapper(IMenu):
    def __init__(self, menubar: QMenuBar, actions: dict[MenubarAction, QAction]):
        self._menubar = menubar
        self._menubar_actions = actions

        self._manager_reference = None

        # self._menubar_actions[MenubarAction.ACTION_NEW].triggered.connect(self._open_new_project)
        self._menubar_actions[MenubarAction.ACTION_NEW].setShortcut(QKeySequence.New)
        self._menubar_actions[MenubarAction.ACTION_NEW].setIcon(self._menubar.style().standardIcon(QStyle.SP_FileIcon))

        # self._menubar_actions[MenubarAction.ACTION_OPEN].triggered.connect(self._open_existing_project)
        self._menubar_actions[MenubarAction.ACTION_OPEN].setShortcut(QKeySequence.Open)
        self._menubar_actions[MenubarAction.ACTION_OPEN].setIcon(self._menubar.style().standardIcon(QStyle.SP_DirIcon))

        # self._menubar_actions[MenubarAction.ACTION_SAVE].triggered.connect(self._save_project)
        self._menubar_actions[MenubarAction.ACTION_SAVE].setShortcut(QKeySequence.Save)
        self._menubar_actions[MenubarAction.ACTION_SAVE].setIcon(self._menubar.style().standardIcon(QStyle.SP_DialogSaveButton))

        # self._menubar_actions[MenubarAction.ACTION_CLOSE].triggered.connect(self._close_project)
        self._menubar_actions[MenubarAction.ACTION_CLOSE].setShortcut(QKeySequence.Close)

        # self._menubar_actions[MenubarAction.ACTION_QUIT].triggered.connect(self._quit_application)
        self._menubar_actions[MenubarAction.ACTION_QUIT].setShortcut(QKeySequence.Quit)
        self._menubar_actions[MenubarAction.ACTION_QUIT].setIcon(self._menubar.style().standardIcon(QStyle.SP_DialogCloseButton))

        # self._menubar_actions[MenubarAction.ACTION_GENERATE].triggered.connect(self._generate_project_files)
        self._menubar_actions[MenubarAction.ACTION_GENERATE].setIcon(self._menubar.style().standardIcon(QStyle.SP_MediaPlay))

        # self._menubar_actions[MenubarAction.ACTION_ABOUT].triggered.connect(self._open_help)
        self._menubar_actions[MenubarAction.ACTION_ABOUT].setIcon(self._menubar.style().standardIcon(QStyle.SP_TitleBarContextHelpButton))
    # __init__


    # ===========================================================================
    # Setters
    # ===========================================================================
    def set_manager_reference(self, manager: IMenuManager) -> None:
        self._manager_reference = manager
    # set_manager_reference


    # ===========================================================================
    # IState functionality
    # ===========================================================================
    def set_state(self, newState: ApplicationState) -> None:
        match newState:
            case ApplicationState.INIT:
                self._menubar.setEnabled(True)
                self._menubar_actions[MenubarAction.ACTION_NEW].setEnabled(True)
                self._menubar_actions[MenubarAction.ACTION_OPEN].setEnabled(True)

                self._menubar_actions[MenubarAction.ACTION_SAVE].setEnabled(False)
                self._menubar_actions[MenubarAction.ACTION_CLOSE].setEnabled(False)
                self._menubar_actions[MenubarAction.ACTION_GENERATE].setEnabled(False)

            case ApplicationState.OPEN:
                self._menubar.setEnabled(True)
                self._menubar_actions[MenubarAction.ACTION_NEW].setEnabled(False)
                self._menubar_actions[MenubarAction.ACTION_OPEN].setEnabled(False)

                self._menubar_actions[MenubarAction.ACTION_SAVE].setEnabled(True)
                self._menubar_actions[MenubarAction.ACTION_CLOSE].setEnabled(True)
                self._menubar_actions[MenubarAction.ACTION_GENERATE].setEnabled(True)

            case ApplicationState.BUSY:
                self._menubar.setEnabled(False)

            case _:
                self._manager_reference.log_message(f"Invalid state: {newState.name}")
    # set_state
