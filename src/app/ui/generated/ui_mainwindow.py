# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLayout,
    QMainWindow, QMenuBar, QSizePolicy, QSplitter,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextEdit,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1086, 734)
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
        self.horizontalSplitter.addWidget(self.projectTree)
        self.propertiesTable = QTableWidget(self.horizontalSplitter)
        if (self.propertiesTable.columnCount() < 2):
            self.propertiesTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.propertiesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.propertiesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.propertiesTable.setObjectName(u"propertiesTable")
        self.horizontalSplitter.addWidget(self.propertiesTable)
        self.propertiesTable.horizontalHeader().setStretchLastSection(True)
        self.propertiesTable.verticalHeader().setVisible(False)
        self.verticalSplitter.addWidget(self.horizontalSplitter)
        self.logger = QTextEdit(self.verticalSplitter)
        self.logger.setObjectName(u"logger")
        self.logger.setFrameShape(QFrame.Shape.NoFrame)
        self.logger.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalSplitter.addWidget(self.logger)

        self.centralWidgetVerticalLayout.addWidget(self.verticalSplitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1086, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Blueprint::Cpp", None))
        ___qtreewidgetitem = self.projectTree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Project", None))
        ___qtablewidgetitem = self.propertiesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Properties", None))
        ___qtablewidgetitem1 = self.propertiesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Values", None))
    # retranslateUi

