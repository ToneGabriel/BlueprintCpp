# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpdialog.ui'
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

class Ui_HelpDialog(object):
    def setupUi(self, HelpDialog):
        if not HelpDialog.objectName():
            HelpDialog.setObjectName(u"HelpDialog")
        HelpDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        HelpDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(HelpDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(HelpDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignTop)

        self.buttonBox = QDialogButtonBox(HelpDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(HelpDialog)
        self.buttonBox.accepted.connect(HelpDialog.accept)
        self.buttonBox.rejected.connect(HelpDialog.reject)

        QMetaObject.connectSlotsByName(HelpDialog)
    # setupUi

    def retranslateUi(self, HelpDialog):
        HelpDialog.setWindowTitle(QCoreApplication.translate("HelpDialog", u"Blueprint::Cpp - About", None))
        self.label.setText(QCoreApplication.translate("HelpDialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Blueprint::Cpp - v3.0.0</span></p><p><span style=\" font-size:14pt;\">TODO: Insert here description</span></p></body></html>", None))
    # retranslateUi

