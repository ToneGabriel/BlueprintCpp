from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QTableWidget, QTableWidgetItem, QStyle, QTextEdit, QLineEdit, QComboBox, QLabel, QCompleter)

from typing import Any, Type

import app.impl as impl
from app.ui.common import DisplayItemType, ApplicationState, TableUIPacket, DisplayItemData
from app.ui.interfaces import ITable, ITableManager


PREFIX_MAP = {
    impl.model.Visibility.PUBLIC: "+",
    impl.model.Visibility.PROTECTED: "#",
    impl.model.Visibility.PRIVATE: "\u2212"
}


class TableWrapper(ITable):
    def __init__(self, uipacket: TableUIPacket):
        self._uipacket = uipacket

        self._manager_reference: ITableManager = None

        self._current_display = DisplayItemType.FOLDER
        self._visibility_dropdown_items = [(member.value, member) for member in impl.model.Visibility]
        self._indirection_dropdown_items = [(member.value, member) for member in impl.model.Indirection]
        self._boolean_dropdown_items = [("False", False), ("True", True)]

        self._default_type_dropdown_items = ["void", "int", "long", "double", "float"]  # TODO: remove this
    # __init__


    # ===========================================================================
    # Setters
    # ===========================================================================
    def set_manager_reference(self, manager: ITableManager) -> None:
        self._manager_reference = manager
    # set_manager_reference


    # ===========================================================================
    # IState functionality
    # ===========================================================================
    def set_state(self, newState: ApplicationState) -> None:
        match newState:
            case ApplicationState.INIT:
                self._uipacket.table.setEnabled(False)

            case ApplicationState.OPEN:
                self._uipacket.table.setEnabled(True)

            case ApplicationState.BUSY:
                self._uipacket.table.setEnabled(False)

            case _:
                self._manager_reference.log_message(f"Invalid state: {newState.name}")
    # set_state


    # ===========================================================================
    # ITable functionality
    # ===========================================================================
    def get_contents(self) -> DisplayItemData:
        ret = DisplayItemData(name=None,
                              prefix=None,
                              updateTreeDisplay=False,
                              itemType=self._current_display,
                              data={}
                              )

        match self._current_display:
            case DisplayItemType.FOLDER:
                pass

            case DisplayItemType.CLASS | DisplayItemType.INTERFACE | DisplayItemType.ENUM:
                ret.name =  self._get_line_table_row_data(0)
                ret.prefix = ""
                ret.updateTreeDisplay = True

                ret.data["description"] = self._get_text_table_row_data(1)

            case DisplayItemType.INHERITANCE:
                ret.name =  self._get_editable_dropdown_table_row_data(0)
                ret.prefix = ""
                ret.updateTreeDisplay = True

                ret.data["type"]        = self._get_editable_dropdown_table_row_data(0)                
                ret.data["visibility"]  = self._get_dropdown_table_row_data(1)
                ret.data["virtual"]     = self._get_dropdown_table_row_data(2)

            case DisplayItemType.MEMBER:
                ret.name =  self._get_line_table_row_data(0)
                ret.prefix = PREFIX_MAP[self._get_dropdown_table_row_data(2)]
                ret.updateTreeDisplay = True

                ret.data["description"] = self._get_text_table_row_data(1)
                ret.data["visibility"]  = self._get_dropdown_table_row_data(2)
                ret.data["type"]        = self._get_editable_dropdown_table_row_data(3)
                ret.data["indirection"] = self._get_dropdown_table_row_data(4)
                ret.data["const"]       = self._get_dropdown_table_row_data(5)
                ret.data["volatile"]    = self._get_dropdown_table_row_data(6)
                ret.data["default"]     = self._get_line_table_row_data(7)

            case DisplayItemType.METHOD:
                ret.name =  self._get_line_table_row_data(0)
                ret.prefix = PREFIX_MAP[self._get_dropdown_table_row_data(2)]
                ret.updateTreeDisplay = True

                ret.data["description"] = self._get_text_table_row_data(1)
                ret.data["visibility"]  = self._get_dropdown_table_row_data(2)
                ret.data["type"]        = self._get_editable_dropdown_table_row_data(3)
                ret.data["indirection"] = self._get_dropdown_table_row_data(4)
                ret.data["const"]       = self._get_dropdown_table_row_data(5)
                ret.data["volatile"]    = self._get_dropdown_table_row_data(6)
                ret.data["immutable"]   = self._get_dropdown_table_row_data(7)
                ret.data["noexcept"]    = self._get_dropdown_table_row_data(8)
                ret.data["override"]    = self._get_dropdown_table_row_data(9)

            case DisplayItemType.PARAMETER:
                ret.name =  self._get_line_table_row_data(0)
                ret.prefix = ""
                ret.updateTreeDisplay = True

                ret.data["description"] = self._get_text_table_row_data(1)
                ret.data["type"]        = self._get_editable_dropdown_table_row_data(2)
                ret.data["indirection"] = self._get_dropdown_table_row_data(3)
                ret.data["const"]       = self._get_dropdown_table_row_data(4)
                ret.data["volatile"]    = self._get_dropdown_table_row_data(5)
                ret.data["default"]     = self._get_line_table_row_data(6)

            case _:
                self._manager_reference.log_message(f"Cannot get data for: {self._current_display.name}")

        return ret
    # get_contents


    def display_contents(self, dataToDisplay:DisplayItemData) -> None:
        match dataToDisplay.itemType:
            case DisplayItemType.FOLDER:
                self._initialise_table_row_count(0)

            case DisplayItemType.CLASS | DisplayItemType.INTERFACE | DisplayItemType.ENUM:
                self._initialise_table_row_count(2)

                self._create_line_table_row(0,              "Name",                                             dataToDisplay.name)
                self._create_text_table_row(1,              "Description",                                      dataToDisplay.data.get("description", ""))

            case DisplayItemType.INHERITANCE:
                self._initialise_table_row_count(3)

                self._create_editable_dropdown_table_row(0, "Type",         self._default_type_dropdown_items,  dataToDisplay.data.get("type", "void"))
                self._create_dropdown_table_row(1,          "Visibility",   self._visibility_dropdown_items,    dataToDisplay.data.get("visibility", impl.model.Visibility.PUBLIC))
                self._create_dropdown_table_row(2,          "Is Virtual",   self._boolean_dropdown_items,       dataToDisplay.data.get("virtual", False))

            case DisplayItemType.MEMBER:
                self._initialise_table_row_count(8)

                self._create_line_table_row(0,              "Name",                                             dataToDisplay.name)
                self._create_text_table_row(1,              "Description",                                      dataToDisplay.data.get("description", ""))
                self._create_dropdown_table_row(2,          "Visibility",   self._visibility_dropdown_items,    dataToDisplay.data.get("visibility", impl.model.Visibility.PRIVATE))
                self._create_editable_dropdown_table_row(3, "Type",         self._default_type_dropdown_items,  dataToDisplay.data.get("type", "void"))
                self._create_dropdown_table_row(4,          "Indirection",  self._indirection_dropdown_items,   dataToDisplay.data.get("indirection", impl.model.Indirection.NONE))
                self._create_dropdown_table_row(5,          "Is Const",     self._boolean_dropdown_items,       dataToDisplay.data.get("const", False))
                self._create_dropdown_table_row(6,          "Is Volatile",  self._boolean_dropdown_items,       dataToDisplay.data.get("volatile", False))
                self._create_line_table_row(7,              "Default Value",                                    dataToDisplay.data.get("default", ""))

            case DisplayItemType.METHOD:
                self._initialise_table_row_count(10)

                self._create_line_table_row(0,              "Name",                                                     dataToDisplay.name)
                self._create_text_table_row(1,              "Description",                                              dataToDisplay.data.get("description", ""))
                self._create_dropdown_table_row(2,          "Visibility",           self._visibility_dropdown_items,    dataToDisplay.data.get("visibility", impl.model.Visibility.PRIVATE))
                self._create_editable_dropdown_table_row(3, "Return Type",          self._default_type_dropdown_items,  dataToDisplay.data.get("type", "void"))
                self._create_dropdown_table_row(4,          "Return Indirection",   self._indirection_dropdown_items,   dataToDisplay.data.get("indirection", impl.model.Indirection.NONE))
                self._create_dropdown_table_row(5,          "Return Is Const",      self._boolean_dropdown_items,       dataToDisplay.data.get("const", False))
                self._create_dropdown_table_row(6,          "Return Is Volatile",   self._boolean_dropdown_items,       dataToDisplay.data.get("volatile", False))
                self._create_dropdown_table_row(7,          "Is Immutable",         self._boolean_dropdown_items,       dataToDisplay.data.get("immutable", False))
                self._create_dropdown_table_row(8,          "Is Noexcept",          self._boolean_dropdown_items,       dataToDisplay.data.get("noexcept", False))
                self._create_dropdown_table_row(9,          "Is Overriden",         self._boolean_dropdown_items,       dataToDisplay.data.get("override", False))

            case DisplayItemType.PARAMETER:
                self._initialise_table_row_count(7)

                self._create_line_table_row(0,              "Name",                                             dataToDisplay.name)
                self._create_text_table_row(1,              "Description",                                      dataToDisplay.data.get("description", ""))
                self._create_editable_dropdown_table_row(2, "Type",         self._default_type_dropdown_items,  dataToDisplay.data.get("type", "void"))
                self._create_dropdown_table_row(3,          "Indirection",  self._indirection_dropdown_items,   dataToDisplay.data.get("indirection", impl.model.Indirection.NONE))
                self._create_dropdown_table_row(4,          "Is Const",     self._boolean_dropdown_items,       dataToDisplay.data.get("const", False))
                self._create_dropdown_table_row(5,          "Is Volatile",  self._boolean_dropdown_items,       dataToDisplay.data.get("volatile", False))
                self._create_line_table_row(6,              "Default Value",                                    dataToDisplay.data.get("default", ""))

            case _:
                self._initialise_table_row_count(0)
                self._manager_reference.log_message(f"Cannot display data for: {dataToDisplay.itemType.name}")

        self._current_display = dataToDisplay.itemType
    # display_contents


    def clear(self) -> None:
        self._clear_table_contents()
    # clear


    # ===========================================================================
    # Helpers
    # ===========================================================================
    def _initialise_table_row_count(self, count: int) -> None:
        if self._uipacket.table.rowCount() > 0:
            self._clear_table_contents()

        self._uipacket.table.setRowCount(count)
    # _initialise_table_row_count


    def _clear_table_contents(self) -> None:
        self._uipacket.table.clearContents()
        self._uipacket.table.setRowCount(0)
    # _clear_table_contents


    def _create_text_table_row(self, row: int, title: str, dataToSet: str) -> None:
        label = QLabel(" " + title + " ")
        textEditor = QTextEdit(dataToSet)

        self._uipacket.table.setRowHeight(row, 150)
        self._uipacket.table.setCellWidget(row, 0, label)
        self._uipacket.table.setCellWidget(row, 1, textEditor)
    # _create_text_table_row


    def _get_text_table_row_data(self, row: int) -> str:
        textEditor: QTextEdit = self._uipacket.table.cellWidget(row, 1)

        if not isinstance(textEditor, QTextEdit):
            return

        return textEditor.toPlainText()
    # _get_text_table_row_data


    def _create_line_table_row(self, row: int, title: str, dataToSet: str) -> None:
        label = QLabel(" " + title + " ")
        lineEditor = QLineEdit(dataToSet)

        self._uipacket.table.setCellWidget(row, 0,label)
        self._uipacket.table.setCellWidget(row, 1, lineEditor)
    # _create_line_table_row


    def _get_line_table_row_data(self, row: int) -> str:
        lineEditor: QLineEdit = self._uipacket.table.cellWidget(row, 1)

        if not isinstance(lineEditor, QLineEdit):
            return

        return lineEditor.text()
    # _get_line_table_row_data


    def _create_dropdown_table_row(self, row: int, title: str, items: list[tuple[str, Any]], dataToSet: Any) -> None:
        label = QLabel(" " + title + " ")
        dropdown = QComboBox()

        for text, value in items:
            dropdown.addItem(text, value)

        index = dropdown.findData(dataToSet)
        if index != -1:
            dropdown.setCurrentIndex(index)

        self._uipacket.table.setCellWidget(row, 0, label)
        self._uipacket.table.setCellWidget(row, 1, dropdown)
    # _create_dropdown_table_row


    def _create_editable_dropdown_table_row(self, row, title: str, items: list[str], dataToSet: str):
        label = QLabel(" " + title + " ")
        dropdown = QComboBox()

        dropdown.setEditable(True)
        completer = dropdown.completer()
        completer.setCompletionMode(QCompleter.PopupCompletion)   # show all matches in a popup list
        completer.setFilterMode(Qt.MatchContains)                 # match substring anywhere in the text
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        for text in items:
            dropdown.addItem(text)

        index = dropdown.findData(dataToSet)
        if index != -1:
            dropdown.setCurrentIndex(index)
        else:
            dropdown.setCurrentIndex(-1)    # no item selected
            dropdown.setEditText(dataToSet) # show the raw value as typed text

        self._uipacket.table.setCellWidget(row, 0, label)
        self._uipacket.table.setCellWidget(row, 1, dropdown)
    # _create_editable_dropdown_table_row


    def _get_dropdown_table_row_data(self, row: int) -> Any:
        dropdown: QComboBox = self._uipacket.table.cellWidget(row, 1)

        if not isinstance(dropdown, QComboBox):
            return

        return dropdown.currentData()
    # _get_dropdown_table_row_data


    def _get_editable_dropdown_table_row_data(self, row: int) -> str:
        dropdown: QComboBox = self._uipacket.table.cellWidget(row, 1)

        if not isinstance(dropdown, QComboBox):
            return

        return dropdown.currentText()
    # _get_editable_dropdown_table_row_data

# TableWrapper
