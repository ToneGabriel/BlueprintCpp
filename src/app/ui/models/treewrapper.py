from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QTreeWidgetItem, QTreeWidget, QStyle, QMenu)

from enum import Enum, Flag, auto
from typing import Any, Type

from app.ui.common import DisplayItemType, ApplicationState, TreeUIPacket
from app.ui.interfaces import (ITree, ITreeManager)


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
    def __init__(self, uipacket: TreeUIPacket):
        self._uipacket = uipacket
        self._tree_menu = QMenu(self._uipacket.tree)

        self._manager_reference: ITreeManager = None

        self._init_tree()
        self._init_tree_menu()
    # __init__


    # ===========================================================================
    # Setters
    # ===========================================================================
    def set_manager_reference(self, manager) -> None:
        self._manager_reference = manager
    # set_manager_reference


    # ===========================================================================
    # IState functionality
    # ===========================================================================
    def set_state(self, newState: ApplicationState) -> None:
        match newState:
            case ApplicationState.INIT:
                self._uipacket.tree.setEnabled(False)
                self._uipacket.treeOptionsWidget.setEnabled(False)

            case ApplicationState.OPEN:
                self._uipacket.tree.setEnabled(True)
                self._uipacket.treeOptionsWidget.setEnabled(True)

            case ApplicationState.BUSY:
                self._uipacket.tree.setEnabled(False)
                self._uipacket.treeOptionsWidget.setEnabled(False)

            case _:
                self._manager_reference.log_message(f"Invalid state: {newState.name}")
    # set_state


    # ===========================================================================
    # ITree functionality
    # ===========================================================================
    def create_root(self, name: str) -> None:
        self._create_tree_object(name, DisplayItemType.FOLDER, None, False)
    # create_root


    def clear(self) -> None:
        self._uipacket.tree.clear()
    # clear_tree


    # ===========================================================================
    # Helpers
    # ===========================================================================
    def _init_tree(self) -> None:
        self._uipacket.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self._uipacket.tree.customContextMenuRequested.connect(self._show_tree_context_menu)
        self._uipacket.tree.currentItemChanged.connect(self._on_tree_item_changed)

        self._uipacket.pushButtonUp.clicked.connect(self._move_tree_object_up)
        self._uipacket.pushButtonUp.setIcon(self._uipacket.tree.style().standardIcon(QStyle.SP_ArrowUp))

        self._uipacket.pushButtonDown.clicked.connect(self._move_tree_object_down)
        self._uipacket.pushButtonDown.setIcon(self._uipacket.tree.style().standardIcon(QStyle.SP_ArrowDown))
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


    def _move_tree_object_up(self) -> None:
        self._move_tree_object(-1)
    # _move_tree_object_up


    def _move_tree_object_down(self) -> None:
        self._move_tree_object(1)
    # _move_tree_object_down


    def _create_tree_object(self,
                            name: str,
                            itemType: DisplayItemType,
                            parentRequiredType: DisplayItemType,
                            isEditable: bool = True
    ) -> None:
        currentItem = self._uipacket.tree.currentItem()
        if currentItem is None:
            currentItem = self._uipacket.tree.invisibleRootItem()

        currentItemType = currentItem.data(0, Qt.UserRole)
        if currentItemType is not None and currentItemType not in parentRequiredType:
            self._manager_reference.log_message(f"Object creation failed: {itemType.name}")
            return

        item = QTreeWidgetItem([name])
        item.setIcon(0, self._uipacket.tree.style().standardIcon(TREE_ITEM_ICON_STYLE_MAP[itemType]))
        item.setData(0, Qt.UserRole, itemType)
        item.setData(0, Qt.UserRole + 1, {})

        if isEditable:
            item.setFlags(item.flags() | Qt.ItemIsEditable)

        # append the item at the end of the same type sublist
        indexToInsert = currentItem.childCount()
        for i in range(currentItem.childCount()):
            if currentItem.child(i).data(0, Qt.UserRole).value > itemType.value:
                indexToInsert = i
                break

        currentItem.insertChild(indexToInsert, item)
    # _create_tree_object


    def _delete_tree_object(self) -> None:
        currentItem = self._uipacket.tree.currentItem()
        parent = currentItem.parent()

        if parent is not None:
            parent.removeChild(currentItem)
        else:
            self._manager_reference.log_message(f"Cannot delete object: {currentItem.text(0)}")
    # _delete_tree_object


    def _move_tree_object(self, offset: int) -> None:
        item = self._uipacket.tree.currentItem()
        if item is None:
            return

        parent = item.parent()
        if parent is None:
            return  # top-level item

        index = parent.indexOfChild(item)
        was_expanded = item.isExpanded()
        itemType = item.data(0, Qt.UserRole)

        parent.takeChild(index)

        # move within the same type sublist
        while (offset > 0 and index < parent.childCount()
            and parent.child(index).data(0, Qt.UserRole).value == itemType.value):
            index += 1
            offset -= 1

        while (offset < 0 and index > 0
            and parent.child(index - 1).data(0, Qt.UserRole).value == itemType.value):
            index -= 1
            offset += 1

        parent.insertChild(index, item)
        item.setExpanded(was_expanded)
        self._uipacket.tree.setCurrentItem(item)
    # _move_tree_object


    def _show_tree_context_menu(self, position) -> None:
        self._tree_menu.exec(self._uipacket.tree.mapToGlobal(position))
    # _show_tree_context_menu


    def _on_tree_item_changed(self, currentItem: QTreeWidgetItem, previousItem: QTreeWidgetItem) -> None:
        # Save data for previous item
        if previousItem:
            previousItem.setData(0, Qt.UserRole + 1, self._manager_reference.get_table_contents())

        # Show data on current item
        if currentItem:
            currentItemType: DisplayItemType = currentItem.data(0, Qt.UserRole)
            currentItemData: dict = currentItem.data(0, Qt.UserRole + 1)
            self._manager_reference.display_table_contents(currentItemType, currentItemData)
    # _on_tree_item_changed

# TreeWrapper
