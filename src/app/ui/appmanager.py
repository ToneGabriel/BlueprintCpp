from typing import Any

from app.ui.common import ApplicationState, DisplayItemType
from app.ui.interfaces import (ILogger, ITree, ITable, IMenu,
                               ILoggerManager, ITreeManager, ITableManager, IMenuManager,
                               IQuit)


class AppManager(ITreeManager, ITableManager, IMenuManager, ILoggerManager):    # Note: ILoggerManager is the last because the rest inherit from it
    def __init__(self):
        self._logger_reference: ILogger = None
        self._tree_reference: ITree = None
        self._table_reference: ITable = None
        self._menu_reference: IMenu = None
        self._quit_reference: IQuit = None
    # __init__


    # ===========================================================================
    # Setters
    # ===========================================================================
    def set_menu_reference(self, menu: IMenu) -> None:
        self._menu_reference = menu
    # set_menu_reference


    def set_logger_reference(self, logger: ILogger) -> None:
        self._logger_reference = logger
    # set_logger_reference


    def set_tree_reference(self, tree: ITree) -> None:
        self._tree_reference = tree
    # set_tree_reference


    def set_table_reference(self, table: ITable) -> None:
        self._table_reference = table
    # set_table_reference


    def set_quit_reference(self, quit: IQuit) -> None:
        self._quit_reference = quit
    # set_quit_reference


    # ===========================================================================
    # IMenuManager functionality
    # ===========================================================================
    def open_project(self) -> None:
        # TODO: implement
        self._set_application_state(ApplicationState.OPEN)
    # open_project


    def open_new_project(self) -> None:
        # TODO: implement
        pass
    # open_new_project


    def open_existing_project(self) -> None:
        # TODO: implement
        pass
    # open_existing_project


    def save_project(self) -> None:
        # TODO: implement
        pass
    # save_project


    def close_project(self) -> None:
        # TODO: implement
        self._set_application_state(ApplicationState.INIT)
    # close_project


    def quit_application(self) -> None:
        self._quit_reference.quit()
    # quit_application


    def generate_project_files(self) -> None:
        # TODO: implement
        pass
    # generate_project_files


    # ===========================================================================
    # ITreeManager functionality
    # ===========================================================================
    def display_table_contents(self, display: DisplayItemType, data: dict[str, Any]) -> None:
        self._table_reference.display_table_contents(display, data)
    # display_table_contents


    def get_table_contents(self) -> dict[str, Any]:
        return self._table_reference.get_table_contents()
    # get_table_contents


    # ===========================================================================
    # ITableManager functionality
    # ===========================================================================
    # TODO: add and implement


    # ===========================================================================
    # ILoggerManager functionality
    # ===========================================================================
    def log_message(self, message: str) -> None:
        self._logger_reference.log_message(message)
    # log_message


    # ===========================================================================
    # Helpers
    # ===========================================================================
    def _set_application_state(self, state: ApplicationState) -> None:
        self._menu_reference.set_state(state)
        self._logger_reference.set_state(state)
        self._tree_reference.set_state(state)
        self._table_reference.set_state(state)
    # _set_application_state

