from enum import Enum, Flag, auto
from typing import Any, Type

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QStyle,
    QTreeWidgetItem, QTableWidgetItem, QFileDialog, QMenu,
    QTextEdit, QComboBox, QTableWidget, QTreeWidget, QLineEdit)


__all__ = [
    "create_text_table_row",
    "get_text_table_row_data",

    "create_line_table_row",
    "get_line_table_row_data",

    "create_dropdown_table_row",
    "get_dropdown_table_row_data",

    "initialise_table_row_count",
    "clear_table_contents"
]


def create_text_table_row(table: QTableWidget, row: int, title: str, dataToSet: str) -> None:
    textEditor = QTextEdit(dataToSet)

    table.setRowHeight(row, 150)
    table.setItem(row, 0, QTableWidgetItem(title))
    table.setCellWidget(row, 1, textEditor)
# create_text_table_row


def get_text_table_row_data(table: QTableWidget, row: int) -> str:
    textEditor: QTextEdit = table.cellWidget(row, 1)

    if not isinstance(textEditor, QTextEdit):
        return

    return textEditor.toPlainText()
# get_text_table_row_data


def create_line_table_row(table: QTableWidget, row: int, title: str, dataToSet: str) -> None:
    lineEditor = QLineEdit(dataToSet)

    table.setItem(row, 0, QTableWidgetItem(title))
    table.setCellWidget(row, 1, lineEditor)
# create_line_table_row


def get_line_table_row_data(table: QTableWidget, row: int) -> str:
    lineEditor: QLineEdit = table.cellWidget(row, 1)

    if not isinstance(lineEditor, QLineEdit):
        return

    return lineEditor.text()
# get_line_table_row_data


def create_dropdown_table_row(table: QTableWidget, row: int, title: str, items: list[tuple[str, Any]], dataToSet: Any) -> None:
    dropdown = QComboBox()
    for text, value in items:
        dropdown.addItem(text, value)

    index = dropdown.findData(dataToSet)
    if index != -1:
        dropdown.setCurrentIndex(index)

    table.setItem(row, 0, QTableWidgetItem(title))
    table.setCellWidget(row, 1, dropdown)
# create_dropdown_table_row


def get_dropdown_table_row_data(table: QTableWidget, row: int) -> Any:
    dropdown: QComboBox = table.cellWidget(row, 1)

    if not isinstance(dropdown, QComboBox):
        return

    return dropdown.currentData()
# get_dropdown_table_row_data


def initialise_table_row_count(table: QTableWidget, count: int) -> None:
    if table.rowCount() == 0:
        table.setRowCount(count)
# initialise_table_row_count


def clear_table_contents(table: QTableWidget) -> None:
    table.clearContents()
    table.setRowCount(0)
# clear_table_contents

