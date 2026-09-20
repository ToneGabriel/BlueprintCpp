from app.ui.common import ApplicationState
from app.ui.interfaces import (ILogger, ITree, ITable, IMenu)


class AppManager:
    def __init__(self):
        self._logger_reference: ILogger = None
        self._tree_reference: ITree = None
        self._table_reference: ITable = None
        self._menu_reference: IMenu = None
    # __init__


    def set_logger_reference(self, logger: ILogger) -> None:
        self._logger_reference = logger
    # set_logger_reference


    def set_tree_reference(self, tree: ITree) -> None:
        self._tree_reference = tree
    # set_tree_reference


    def set_table_reference(self, table: ITable) -> None:
        self._table_reference = table
    # set_table_reference


    def set_menu_reference(self, menu: IMenu) -> None:
        self._menu_reference = menu
    # set_menu_reference


    def open_project(self) -> None:
        self._set_application_state(ApplicationState.OPEN)
    # open_project


    def _set_application_state(self, state: ApplicationState) -> None:
        self._tree_reference.set_state(state)
        self._table_reference.set_state(state)
        self._logger_reference.set_state(state)
        self._menu_reference.set_state(state)
    # _set_application_state

