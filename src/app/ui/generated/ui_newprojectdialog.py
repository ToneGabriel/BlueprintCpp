# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newprojectdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_NewProjectDialog(object):
    def setupUi(self, NewProjectDialog):
        if not NewProjectDialog.objectName():
            NewProjectDialog.setObjectName(u"NewProjectDialog")
        NewProjectDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        NewProjectDialog.resize(470, 186)
        self.verticalLayout = QVBoxLayout(NewProjectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.projectNameLabel = QLabel(NewProjectDialog)
        self.projectNameLabel.setObjectName(u"projectNameLabel")

        self.verticalLayout.addWidget(self.projectNameLabel)

        self.projectNameText = QLineEdit(NewProjectDialog)
        self.projectNameText.setObjectName(u"projectNameText")

        self.verticalLayout.addWidget(self.projectNameText)

        self.projectSavePathLabel = QLabel(NewProjectDialog)
        self.projectSavePathLabel.setObjectName(u"projectSavePathLabel")

        self.verticalLayout.addWidget(self.projectSavePathLabel)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.projectSavePathText = QLineEdit(NewProjectDialog)
        self.projectSavePathText.setObjectName(u"projectSavePathText")

        self.horizontalLayout_1.addWidget(self.projectSavePathText)

        self.browseButton = QPushButton(NewProjectDialog)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setMinimumSize(QSize(0, 24))

        self.horizontalLayout_1.addWidget(self.browseButton)


        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(NewProjectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(NewProjectDialog)
        self.buttonBox.accepted.connect(NewProjectDialog.accept)
        self.buttonBox.rejected.connect(NewProjectDialog.reject)

        QMetaObject.connectSlotsByName(NewProjectDialog)
    # setupUi

    def retranslateUi(self, NewProjectDialog):
        NewProjectDialog.setWindowTitle(QCoreApplication.translate("NewProjectDialog", u"Blueprint::Cpp - New Project", None))
        self.projectNameLabel.setText(QCoreApplication.translate("NewProjectDialog", u"Project name", None))
        self.projectSavePathLabel.setText(QCoreApplication.translate("NewProjectDialog", u"Project path", None))
        self.browseButton.setText(QCoreApplication.translate("NewProjectDialog", u"Browse...", None))
    # retranslateUi

