from PySide6.QtWidgets import QTextEdit, QMenuBar, QTreeWidget, QTableWidget, QDialog, QPushButton, QLineEdit
from PySide6.QtGui import QAction, QKeySequence

from dataclasses import dataclass


__all__ = [
    "TreeUIPacket",
    "TableUIPacket",
    "LoggerUIPacket",
    "MenubarUIPacket",
    "NewProjectDialogUIPacket",
    "CloseProjectDialogUIPacket",
    "HelpDialogUIPacket"
]


@dataclass
class TreeUIPacket:
    tree: QTreeWidget


@dataclass
class TableUIPacket:
    table: QTableWidget


@dataclass
class LoggerUIPacket:
    logger: QTextEdit


@dataclass
class MenubarUIPacket:
    menubar: QMenuBar
    actionNew: QAction
    actionOpen: QAction
    actionSave: QAction
    actionClose: QAction
    actionQuit: QAction
    actionGenerate: QAction
    actionAbout: QAction


@dataclass
class NewProjectDialogUIPacket:
    dialog: QDialog
    browseButton: QPushButton
    projectNameText: QLineEdit
    projectSavePathText: QLineEdit


@dataclass
class CloseProjectDialogUIPacket:
    dialog: QDialog


@dataclass
class HelpDialogUIPacket:
    dialog: QDialog

