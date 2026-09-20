from PySide6.QtWidgets import (QTextEdit)

from app.ui.common import ApplicationState
from app.ui.interfaces import ILogger, IMenu


class MenuWrapper(IMenu):
    def __init__(self):
        self._logger_reference = None
    # __init__


    def set_logger_reference(self, logger: ILogger) -> None:
        self._logger_reference = logger
    # set_logger_reference


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
                self._logger_reference.log_message(f"Invalid state: {newState.name}")
    # set_state


