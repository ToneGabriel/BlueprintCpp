# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLayout,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSplitter, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1086, 734)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionGenerate = QAction(MainWindow)
        self.actionGenerate.setObjectName(u"actionGenerate")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralWidgetVerticalLayout = QVBoxLayout(self.centralwidget)
        self.centralWidgetVerticalLayout.setSpacing(0)
        self.centralWidgetVerticalLayout.setObjectName(u"centralWidgetVerticalLayout")
        self.centralWidgetVerticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.centralWidgetVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSplitter = QSplitter(self.centralwidget)
        self.verticalSplitter.setObjectName(u"verticalSplitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalSplitter.sizePolicy().hasHeightForWidth())
        self.verticalSplitter.setSizePolicy(sizePolicy1)
        self.verticalSplitter.setAutoFillBackground(False)
        self.verticalSplitter.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalSplitter.setOrientation(Qt.Orientation.Vertical)
        self.verticalSplitter.setOpaqueResize(True)
        self.verticalSplitter.setHandleWidth(4)
        self.horizontalSplitter = QSplitter(self.verticalSplitter)
        self.horizontalSplitter.setObjectName(u"horizontalSplitter")
        self.horizontalSplitter.setOrientation(Qt.Orientation.Horizontal)
        self.projectTree = QTreeWidget(self.horizontalSplitter)
        self.projectTree.setObjectName(u"projectTree")
        self.projectTree.setFrameShape(QFrame.Shape.StyledPanel)
        self.projectTree.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalSplitter.addWidget(self.projectTree)
        self.propertiesTable = QTableWidget(self.horizontalSplitter)
        if (self.propertiesTable.columnCount() < 2):
            self.propertiesTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.propertiesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.propertiesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.propertiesTable.setObjectName(u"propertiesTable")
        self.propertiesTable.setFrameShape(QFrame.Shape.StyledPanel)
        self.propertiesTable.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalSplitter.addWidget(self.propertiesTable)
        self.propertiesTable.horizontalHeader().setStretchLastSection(True)
        self.propertiesTable.verticalHeader().setVisible(False)
        self.verticalSplitter.addWidget(self.horizontalSplitter)
        self.loggTextWindow = QTextEdit(self.verticalSplitter)
        self.loggTextWindow.setObjectName(u"loggTextWindow")
        self.loggTextWindow.setFrameShape(QFrame.Shape.StyledPanel)
        self.loggTextWindow.setFrameShadow(QFrame.Shadow.Sunken)
        self.loggTextWindow.setReadOnly(True)
        self.verticalSplitter.addWidget(self.loggTextWindow)

        self.centralWidgetVerticalLayout.addWidget(self.verticalSplitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1086, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)
        self.menuOptions.addAction(self.actionGenerate)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Blueprint::Cpp", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
        self.actionGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate...", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        ___qtreewidgetitem = self.projectTree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Project Tree", None))
        ___qtablewidgetitem = self.propertiesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Properties", None))
        ___qtablewidgetitem1 = self.propertiesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Values", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

