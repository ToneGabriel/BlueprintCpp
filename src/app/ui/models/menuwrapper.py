from PySide6.QtWidgets import QTextEdit, QMenuBar, QStyle
from PySide6.QtGui import QAction, QKeySequence

from app.ui.common import ApplicationState, MenubarUIPacket, NewProjectDialogUIPacket, CloseProjectDialogUIPacket, HelpDialogUIPacket
from app.ui.interfaces import IMenu, IMenuManager


class MenuWrapper(IMenu):
    def __init__(self,
                 menubarUIPacket: MenubarUIPacket,
                 newProjectDialogUIPacket: NewProjectDialogUIPacket,
                 closeProjectDialogUIPacket: CloseProjectDialogUIPacket,
                 helpDialogUIPacket: HelpDialogUIPacket
    ):
        self._menubarUIPacket = menubarUIPacket
        self._newProjectDialogUIPacket = newProjectDialogUIPacket
        self._closeProjectDialogUIPacket = closeProjectDialogUIPacket
        self._helpDialogUIPacket = helpDialogUIPacket

        self._manager_reference = None

        # initialization
        # self._menubarUIPacket.actionNew.triggered.connect(self._open_new_project)
        self._menubarUIPacket.actionNew.setShortcut(QKeySequence.New)
        self._menubarUIPacket.actionNew.setIcon(self._menubarUIPacket.menubar.style().standardIcon(QStyle.SP_FileIcon))

        # self._menubarUIPacket.actionOpen.triggered.connect(self._open_existing_project)
        self._menubarUIPacket.actionOpen.setShortcut(QKeySequence.Open)
        self._menubarUIPacket.actionOpen.setIcon(self._menubarUIPacket.menubar.style().standardIcon(QStyle.SP_DirIcon))

        self._menubarUIPacket.actionSave.triggered.connect(self._save_project)
        self._menubarUIPacket.actionSave.setShortcut(QKeySequence.Save)
        self._menubarUIPacket.actionSave.setIcon(self._menubarUIPacket.menubar.style().standardIcon(QStyle.SP_DialogSaveButton))

        self._menubarUIPacket.actionClose.triggered.connect(self._close_project)
        self._menubarUIPacket.actionClose.setShortcut(QKeySequence.Close)

        self._menubarUIPacket.actionQuit.triggered.connect(self._quit_application)
        self._menubarUIPacket.actionQuit.setShortcut(QKeySequence.Quit)
        self._menubarUIPacket.actionQuit.setIcon(self._menubarUIPacket.menubar.style().standardIcon(QStyle.SP_DialogCloseButton))

        self._menubarUIPacket.actionGenerate.triggered.connect(self._generate_project_files)
        self._menubarUIPacket.actionGenerate.setIcon(self._menubarUIPacket.menubar.style().standardIcon(QStyle.SP_MediaPlay))

        self._menubarUIPacket.actionAbout.triggered.connect(self._open_help)
        self._menubarUIPacket.actionAbout.setIcon(self._menubarUIPacket.menubar.style().standardIcon(QStyle.SP_TitleBarContextHelpButton))
    # __init__


    # ===========================================================================
    # Setters
    # ===========================================================================
    def set_manager_reference(self, manager: IMenuManager) -> None:
        self._manager_reference = manager
    # set_manager_reference


    # ===========================================================================
    # IState functionality
    # ===========================================================================
    def set_state(self, newState: ApplicationState) -> None:
        match newState:
            case ApplicationState.INIT:
                self._menubarUIPacket.menubar.setEnabled(True)
                self._menubarUIPacket.actionNew.setEnabled(True)
                self._menubarUIPacket.actionOpen.setEnabled(True)

                self._menubarUIPacket.actionSave.setEnabled(False)
                self._menubarUIPacket.actionClose.setEnabled(False)
                self._menubarUIPacket.actionGenerate.setEnabled(False)

            case ApplicationState.OPEN:
                self._menubarUIPacket.menubar.setEnabled(True)
                self._menubarUIPacket.actionNew.setEnabled(False)
                self._menubarUIPacket.actionOpen.setEnabled(False)

                self._menubarUIPacket.actionSave.setEnabled(True)
                self._menubarUIPacket.actionClose.setEnabled(True)
                self._menubarUIPacket.actionGenerate.setEnabled(True)

            case ApplicationState.BUSY:
                self._menubarUIPacket.menubar.setEnabled(False)

            case _:
                self._manager_reference.log_message(f"Invalid state: {newState.name}")
    # set_state


    # ===========================================================================
    # Helpers
    # ===========================================================================
    def _save_project(self) -> None:
        self._manager_reference.save_project()
    # _save_project


    def _close_project(self) -> None:
        self._manager_reference.close_project()
    # _close_project


    def _generate_project_files(self) -> None:
        self._manager_reference.generate_project_files()
    # _generate_project_files


    def _quit_application(self) -> None:
        self._manager_reference.quit_application()
    # _quit_application


    def _open_help(self) -> None:
        self._helpDialogUIPacket.dialog.exec()
    # _open_help

