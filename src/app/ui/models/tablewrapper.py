from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QTableWidget, QTableWidgetItem, QStyle, QTextEdit, QLineEdit, QComboBox, QLabel)

from typing import Any, Type

import app.impl as impl
from app.ui.common import DisplayItemType, ApplicationState
from app.ui.interfaces import ILogger, ITable


class TableWrapper(ITable):
    def __init__(self, table: QTableWidget):
        self._table = table

        self._logger_reference = None

        self._current_display = DisplayItemType.FOLDER
        self._visibility_dropdown_items = [(member.value, member) for member in impl.model.Visibility]
        self._indirection_dropdown_items = [(member.value, member) for member in impl.model.Indirection]
        self._boolean_dropdown_items = [("False", False), ("True", True)]
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


    def get_table_contents(self) -> dict[str, Any]:
        data = {}

        match self._current_display:
            case DisplayItemType.FOLDER:
                pass

            case DisplayItemType.CLASS | DisplayItemType.INTERFACE | DisplayItemType.ENUM:
                data["description"] = self._get_text_table_row_data(0)

            case DisplayItemType.MEMBER:
                data["description"] = self._get_text_table_row_data(0)
                data["visibility"]  = self._get_dropdown_table_row_data(1)
                data["type"]        = self._get_line_table_row_data(2)
                data["indirection"] = self._get_dropdown_table_row_data(3)
                data["const"]       = self._get_dropdown_table_row_data(4)
                data["volatile"]    = self._get_dropdown_table_row_data(5)
                data["default"]     = self._get_line_table_row_data(6)

            case DisplayItemType.METHOD:
                data["description"] = self._get_text_table_row_data(0)
                data["visibility"]  = self._get_dropdown_table_row_data(1)
                data["type"]        = self._get_line_table_row_data(2)
                data["indirection"] = self._get_dropdown_table_row_data(3)
                data["const"]       = self._get_dropdown_table_row_data(4)
                data["volatile"]    = self._get_dropdown_table_row_data(5)
                data["immutable"]   = self._get_dropdown_table_row_data(6)
                data["noexcept"]    = self._get_dropdown_table_row_data(7)
                data["override"]    = self._get_dropdown_table_row_data(8)

            case DisplayItemType.PARAMETER:
                data["description"] = self._get_text_table_row_data(0)
                data["type"]        = self._get_line_table_row_data(1)
                data["indirection"] = self._get_dropdown_table_row_data(2)
                data["const"]       = self._get_dropdown_table_row_data(3)
                data["volatile"]    = self._get_dropdown_table_row_data(4)
                data["default"]     = self._get_line_table_row_data(5)

            case _:
                self._logger_reference.log_message(f"Cannot get data for: {self._current_display.name}")

        return data
    # get_table_contents


    def display_table_contents(self, display: DisplayItemType, data: dict[str, Any]) -> None:
        match display:
            case DisplayItemType.FOLDER:
                pass

            case DisplayItemType.CLASS | DisplayItemType.INTERFACE | DisplayItemType.ENUM:
                self._initialise_table_row_count(1)

                self._create_text_table_row(0,      "Description",                                  data.get("description", ""))

            case DisplayItemType.MEMBER:
                self._initialise_table_row_count(7)

                self._create_text_table_row(0,      "Description",                                   data.get("description", ""))
                self._create_dropdown_table_row(1,  "Visibility",  self._visibility_dropdown_items,  data.get("visibility", impl.model.Visibility.PRIVATE))
                self._create_line_table_row(2,      "Type",                                          data.get("type", "void"))
                self._create_dropdown_table_row(3,  "Indirection", self._indirection_dropdown_items, data.get("indirection", impl.model.Indirection.NONE))
                self._create_dropdown_table_row(4,  "Is Const",    self._boolean_dropdown_items,     data.get("const", False))
                self._create_dropdown_table_row(5,  "Is Volatile", self._boolean_dropdown_items,     data.get("volatile", False))
                self._create_line_table_row(6,      "Default Value",                                 data.get("default", ""))

            case DisplayItemType.METHOD:
                self._initialise_table_row_count(9)

                self._create_text_table_row(0,      "Description",                                    data.get("description", ""))
                self._create_dropdown_table_row(1,  "Visibility",   self._visibility_dropdown_items,  data.get("visibility", impl.model.Visibility.PRIVATE))
                self._create_line_table_row(2,      "Return Type",                                    data.get("type", "void"))
                self._create_dropdown_table_row(3,  "Indirection",  self._indirection_dropdown_items, data.get("indirection", impl.model.Indirection.NONE))
                self._create_dropdown_table_row(4,  "Is Const",     self._boolean_dropdown_items,     data.get("const", False))
                self._create_dropdown_table_row(5,  "Is Volatile",  self._boolean_dropdown_items,     data.get("volatile", False))
                self._create_dropdown_table_row(6,  "Is Immutable", self._boolean_dropdown_items,     data.get("immutable", False))
                self._create_dropdown_table_row(7,  "Is Noexcept",  self._boolean_dropdown_items,     data.get("noexcept", False))
                self._create_dropdown_table_row(8,  "Is Overriden", self._boolean_dropdown_items,     data.get("override", False))

            case DisplayItemType.PARAMETER:
                self._initialise_table_row_count(6)

                self._create_text_table_row(0,      "Description",                                   data.get("description", ""))
                self._create_line_table_row(1,      "Type",                                          data.get("type", "void"))
                self._create_dropdown_table_row(2,  "Indirection", self._indirection_dropdown_items, data.get("indirection", impl.model.Indirection.NONE))
                self._create_dropdown_table_row(3,  "Is Const",    self._boolean_dropdown_items,     data.get("const", False))
                self._create_dropdown_table_row(4,  "Is Volatile", self._boolean_dropdown_items,     data.get("volatile", False))
                self._create_line_table_row(5,      "Default Value",                                 data.get("default", ""))

            case _:
                self._logger_reference.log_message(f"Cannot display data for: {display.name}")

        self._current_display = display
    # display_table_contents


    def _initialise_table_row_count(self, count: int) -> None:
        if self._table.rowCount() > 0:
            self._clear_table_contents()

        self._table.setRowCount(count)
    # _initialise_table_row_count


    def _clear_table_contents(self) -> None:
        self._table.clearContents()
        self._table.setRowCount(0)
    # _clear_table_contents


    def _create_text_table_row(self, row: int, title: str, dataToSet: str) -> None:
        label = QLabel(title)
        textEditor = QTextEdit(dataToSet)

        self._table.setRowHeight(row, 150)
        self._table.setCellWidget(row, 0, label)
        self._table.setCellWidget(row, 1, textEditor)
    # _create_text_table_row


    def _get_text_table_row_data(self, row: int) -> str:
        textEditor: QTextEdit = self._table.cellWidget(row, 1)

        if not isinstance(textEditor, QTextEdit):
            return

        return textEditor.toPlainText()
    # _get_text_table_row_data


    def _create_line_table_row(self, row: int, title: str, dataToSet: str) -> None:
        label = QLabel(title)
        lineEditor = QLineEdit(dataToSet)

        self._table.setCellWidget(row, 0,label)
        self._table.setCellWidget(row, 1, lineEditor)
    # _create_line_table_row


    def _get_line_table_row_data(self, row: int) -> str:
        lineEditor: QLineEdit = self._table.cellWidget(row, 1)

        if not isinstance(lineEditor, QLineEdit):
            return

        return lineEditor.text()
    # _get_line_table_row_data


    def _create_dropdown_table_row(self, row: int, title: str, items: list[tuple[str, Any]], dataToSet: Any) -> None:
        label = QLabel(title)
        dropdown = QComboBox()

        for text, value in items:
            dropdown.addItem(text, value)

        index = dropdown.findData(dataToSet)
        if index != -1:
            dropdown.setCurrentIndex(index)

        self._table.setCellWidget(row, 0, label)
        self._table.setCellWidget(row, 1, dropdown)
    # _create_dropdown_table_row


    def _get_dropdown_table_row_data(self, row: int) -> Any:
        dropdown: QComboBox = self._table.cellWidget(row, 1)

        if not isinstance(dropdown, QComboBox):
            return

        return dropdown.currentData()
    # _get_dropdown_table_row_data