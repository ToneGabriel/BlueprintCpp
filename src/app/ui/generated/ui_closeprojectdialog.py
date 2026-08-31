# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'closeprojectdialog.ui'
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
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CloseProjectDialog(object):
    def setupUi(self, CloseProjectDialog):
        if not CloseProjectDialog.objectName():
            CloseProjectDialog.setObjectName(u"CloseProjectDialog")
        CloseProjectDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        CloseProjectDialog.resize(410, 120)
        self.verticalLayout = QVBoxLayout(CloseProjectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.closeInfoLabel = QLabel(CloseProjectDialog)
        self.closeInfoLabel.setObjectName(u"closeInfoLabel")

        self.verticalLayout.addWidget(self.closeInfoLabel)

        self.buttonBox = QDialogButtonBox(CloseProjectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(CloseProjectDialog)
        self.buttonBox.accepted.connect(CloseProjectDialog.accept)
        self.buttonBox.rejected.connect(CloseProjectDialog.reject)

        QMetaObject.connectSlotsByName(CloseProjectDialog)
    # setupUi

    def retranslateUi(self, CloseProjectDialog):
        CloseProjectDialog.setWindowTitle(QCoreApplication.translate("CloseProjectDialog", u"Blueprint::Cpp - Close project", None))
        self.closeInfoLabel.setText(QCoreApplication.translate("CloseProjectDialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Close the project?</span></p><p><span style=\" font-size:14pt;\">Unsaved data will be lost...</span></p></body></html>", None))
    # retranslateUi

