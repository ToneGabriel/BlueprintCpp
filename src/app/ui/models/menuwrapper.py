from PySide6.QtWidgets import (QTextEdit, QMenuBar)
from PySide6.QtGui import QAction

from app.ui.common import ApplicationState, MenubarAction
from app.ui.interfaces import IMenu, IMenuManager


class MenuWrapper(IMenu):
    def __init__(self, menubar: QMenuBar, actions: dict[MenubarAction, QAction]):
        self._menubar = menubar
        self._menubar_actions = actions

        self._manager_reference = None
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
