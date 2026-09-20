from PySide6.QtWidgets import (QTextEdit)

from datetime import datetime

from app.ui.common import ApplicationState
from app.ui.interfaces import ILogger


class LoggerWrapper(ILogger):
    def __init__(self, logger: QTextEdit):
        self._logger = logger
    # __init__


    def set_state(self, newState: ApplicationState) -> None:
        # logger will always be active
        return
    # set_state


    def log_message(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._logger.append(f"[{timestamp}] - {message}")
    # _log_message


    def clear_logs(self) -> None:
        self._logger.clear()
    # clear_logs

