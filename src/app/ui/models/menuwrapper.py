from PySide6.QtWidgets import (QTextEdit)
from PySide6.QtGui import QAction

from app.ui.common import ApplicationState, MenubarAction
from app.ui.interfaces import IMenu, IMenuManager


class MenuWrapper(IMenu):
    def __init__(self, actions: dict[MenubarAction, QAction]):
        self._menubar_actions = actions

        self._manager_reference = None
    # __init__


    def set_manager_reference(self, manager: IMenuManager) -> None:
        self._manager_reference = manager
    # set_manager_reference


    def set_state(self, newState: ApplicationState) -> None:
        # TODO: implement

        match newState:
            case ApplicationState.INIT:
                pass

            case ApplicationState.OPEN:
                pass

            case ApplicationState.BUSY:
                pass

            case _:
                self._manager_reference.log_message(f"Invalid state: {newState.name}")
    # set_state


