from PySide6.QtWidgets import (QTextEdit)

from datetime import datetime

from app.ui.common import ApplicationState, LoggerUIPacket
from app.ui.interfaces import ILogger, ILoggerManager


class LoggerWrapper(ILogger):
    def __init__(self, uipacket: LoggerUIPacket):
        self._uipacket = uipacket

        self._manager_reference = None
    # __init__


    # ===========================================================================
    # Setters
    # ===========================================================================
    def set_manager_reference(self, manager: ILoggerManager) -> None:
        self._manager_reference = manager
    # set_manager_reference


    # ===========================================================================
    # IState functionality
    # ===========================================================================
    def set_state(self, newState: ApplicationState) -> None:
        # logger will always be active
        return
    # set_state


    # ===========================================================================
    # ILogger functionality
    # ===========================================================================
    def log_message(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._uipacket.logger.append(f"[{timestamp}] - {message}")
    # _log_message


    def clear_logs(self) -> None:
        self._uipacket.logger.clear()
    # clear_logs

# LoggerWrapper
