from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QTreeWidgetItem, QTreeWidget, QStyle, QMenu)

from enum import Enum, Flag, auto
from typing import Any, Type

from app.ui.common import DisplayItemType, ApplicationState
from app.ui.interfaces import (ITree, ITable, ILogger)


TREE_ITEM_ICON_STYLE_MAP = {
    DisplayItemType.FOLDER:         QStyle.SP_DirIcon,
    DisplayItemType.CLASS:          QStyle.SP_FileIcon,
    DisplayItemType.INTERFACE:      QStyle.SP_FileIcon,
    DisplayItemType.ENUM:           QStyle.SP_FileIcon,
    DisplayItemType.INHERITANCE:    QStyle.SP_FileIcon, # TODO: change
    DisplayItemType.MEMBER:         QStyle.SP_TitleBarNormalButton,
    DisplayItemType.METHOD:         QStyle.SP_ToolBarHorizontalExtensionButton,
    DisplayItemType.PARAMETER:      QStyle.SP_TitleBarNormalButton
}


class TreeWrapper(ITree):
    def __init__(self, tree: QTreeWidget):
        self._tree = tree
        self._tree_menu = QMenu(self._tree)

        self._table_reference: ITable = None
        self._logger_reference: ILogger = None

        self._init_tree()
        self._init_tree_menu()
    # __init__


    def set_table_reference(self, table: ITable) -> None:
        self._table_reference = table
    # set_table_reference


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


    def _init_tree(self) -> None:
        self._tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self._tree.customContextMenuRequested.connect(self._show_tree_context_menu)
        self._tree.currentItemChanged.connect(self._on_tree_item_changed)
    # _init_tree


    def _init_tree_menu(self) -> None:
        createSubmenu = self._tree_menu.addMenu("Create...")

        createSubmenu.addAction("Folder",    self._create_folder_tree_object)
        createSubmenu.addAction("Class",     self._create_class_tree_object)
        createSubmenu.addAction("Interface", self._create_interface_tree_object)
        createSubmenu.addAction("Enum",      self._create_enum_tree_object)
        createSubmenu.addAction("Member",    self._create_member_tree_object)
        createSubmenu.addAction("Method",    self._create_method_tree_object)
        createSubmenu.addAction("Parameter", self._create_parameter_tree_object)

        self._tree_menu.addAction("Delete", self._delete_tree_object)
    # _init_tree_menu


    def _create_folder_tree_object(self) -> None:
        self._create_tree_object("NewFolder", DisplayItemType.FOLDER, DisplayItemType.FOLDER)
    # _create_folder_tree_object


    def _create_class_tree_object(self) -> None:
        self._create_tree_object("NewClass", DisplayItemType.CLASS, DisplayItemType.FOLDER)
    # _create_class_tree_object


    def _create_interface_tree_object(self) -> None:
        self._create_tree_object("NewInterface", DisplayItemType.INTERFACE, DisplayItemType.FOLDER)
    # _create_interface_tree_object


    def _create_enum_tree_object(self) -> None:
        self._create_tree_object("NewEnum", DisplayItemType.ENUM, DisplayItemType.FOLDER)
    # _create_enum_tree_object


    def _create_member_tree_object(self) -> None:
        self._create_tree_object("NewMember", DisplayItemType.MEMBER, DisplayItemType.CLASS)
    # _create_member_tree_object


    def _create_method_tree_object(self) -> None:
        self._create_tree_object("NewMethod", DisplayItemType.METHOD, DisplayItemType.CLASS | DisplayItemType.INTERFACE)
    # _create_method_tree_object


    def _create_parameter_tree_object(self) -> None:
        self._create_tree_object("NewParameter", DisplayItemType.PARAMETER, DisplayItemType.METHOD)
    # _create_parameter_tree_object


    def _create_tree_object(self,
                            name: str,
                            type: DisplayItemType,
                            parentRequiredType: DisplayItemType,
                            isEditable: bool = True
    ) -> None:
        currentItem = self._tree.currentItem()
        if currentItem is None:
            currentItem = self._tree.invisibleRootItem()

        currentItemType = currentItem.data(0, Qt.UserRole)
        if currentItemType is not None and currentItemType not in parentRequiredType:
            self._logger_reference.log_message(f"Object creation failed: {type.name}")
            return

        item = QTreeWidgetItem([name])
        item.setIcon(0, self._tree.style().standardIcon(TREE_ITEM_ICON_STYLE_MAP[type]))
        item.setData(0, Qt.UserRole, type)
        item.setData(0, Qt.UserRole + 1, {})

        if isEditable:
            item.setFlags(item.flags() | Qt.ItemIsEditable)

        currentItem.addChild(item)
    # _create_tree_object


    def _delete_tree_object(self) -> None:
        currentItem = self._tree.currentItem()
        parent = currentItem.parent()

        if parent is not None:
            parent.removeChild(currentItem)
        else:
            self._logger_reference.log_message(f"Cannot delete object: {currentItem.text(0)}")
    # _delete_tree_object


    def _show_tree_context_menu(self, position) -> None:
        self._tree_menu.exec(self._tree.mapToGlobal(position))
    # _show_tree_context_menu


    def _on_tree_item_changed(self, currentItem: QTreeWidgetItem, previousItem: QTreeWidgetItem) -> None:
        # Save data for previous item
        if previousItem:
            previousItem.setData(0, Qt.UserRole + 1, self._table_reference.get_table_contents())

        # Show data on current item
        if currentItem:
            currentItemType: DisplayItemType = currentItem.data(0, Qt.UserRole)
            currentItemData: dict = currentItem.data(0, Qt.UserRole + 1)
            self._table_reference.display_table_contents(currentItemType, currentItemData)
    # _on_tree_item_changed
