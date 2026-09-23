from typing import Any
from pathlib import Path

from app.ui.common import ApplicationState, DisplayItemType, DisplayItemData
from app.ui.interfaces import (ILogger, ITree, ITable, IMenu,
                               ILoggerManager, ITreeManager, ITableManager, IMenuManager,
                               IQtRoot)


class AppManager(ITreeManager, ITableManager, IMenuManager, ILoggerManager):    # Note: ILoggerManager is the last because the rest inherit from it
    def __init__(self):
        # internal data
        self._project_name = ""
        self._project_path = ""

        # references
        self._logger_reference: ILogger = None
        self._tree_reference: ITree = None
        self._table_reference: ITable = None
        self._menu_reference: IMenu = None
        self._qt_root_reference: IQtRoot = None
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


    def set_qt_root_reference(self, qt_root: IQtRoot) -> None:
        self._qt_root_reference = qt_root
    # set_qt_root_reference


    # ===========================================================================
    # Entry point
    # ===========================================================================
    def run(self) -> None:
        self._set_application_state(ApplicationState.INIT)
        self._qt_root_reference.run()
    # run


    # ===========================================================================
    # IMenuManager functionality
    # ===========================================================================
    def open_new_project(self, name: str, path: str) -> None:
        if name == "" or path == "" or not Path(path).exists():
            self.log_message("Invalid project name or path")
        else:
            self._project_name = name
            self._project_path = path

            self._tree_reference.create_root(name)

            self._set_application_state(ApplicationState.OPEN)
    # open_new_project


    def open_existing_project(self, path: str) -> None:
        # TODO: implement
        # self._set_application_state(ApplicationState.OPEN)
        pass
    # open_existing_project


    def save_project(self) -> None:
        # TODO: implement
        pass
    # save_project


    def close_project(self) -> None:
        self._tree_reference.clear()
        self._table_reference.clear()
        self._set_application_state(ApplicationState.INIT)
    # close_project


    def quit_application(self) -> None:
        self.close_project()
        self._qt_root_reference.quit()
    # quit_application


    def generate_project_files(self) -> None:
        # TODO: implement
        pass
    # generate_project_files


    # ===========================================================================
    # ITreeManager functionality
    # ===========================================================================
    def display_table_contents(self, dataToDisplay: DisplayItemData) -> None:
        self._table_reference.display_contents(dataToDisplay)
    # display_table_contents


    def get_table_contents(self) -> DisplayItemData:
        return self._table_reference.get_contents()
    # get_table_contents


    # ===========================================================================
    # ITableManager functionality
    # ===========================================================================
    # None so far


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

# AppManager
