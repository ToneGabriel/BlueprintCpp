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
# TreeUIPacket


@dataclass
class TableUIPacket:
    table: QTableWidget
# TableUIPacket


@dataclass
class LoggerUIPacket:
    logger: QTextEdit
# LoggerUIPacket


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
# MenubarUIPacket


@dataclass
class NewProjectDialogUIPacket:
    dialog: QDialog
    browseButton: QPushButton
    projectNameText: QLineEdit
    projectSavePathText: QLineEdit
# NewProjectDialogUIPacket


@dataclass
class CloseProjectDialogUIPacket:
    dialog: QDialog
# CloseProjectDialogUIPacket


@dataclass
class HelpDialogUIPacket:
    dialog: QDialog
# HelpDialogUIPacket
