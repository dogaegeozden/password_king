# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'credits_dialog_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreditsDialog(object):
    def setupUi(self, CreditsDialog):
        if not CreditsDialog.objectName():
            CreditsDialog.setObjectName(u"CreditsDialog")
        CreditsDialog.resize(400, 210)
        CreditsDialog.setStyleSheet(u"#centralwidget {\n"
"}")
        self.actionUser_Name_Generator = QAction(CreditsDialog)
        self.actionUser_Name_Generator.setObjectName(u"actionUser_Name_Generator")
        self.actionPassword_Generator = QAction(CreditsDialog)
        self.actionPassword_Generator.setObjectName(u"actionPassword_Generator")
        self.actionPassword_Manager = QAction(CreditsDialog)
        self.actionPassword_Manager.setObjectName(u"actionPassword_Manager")
        self.credits_label = QLabel(CreditsDialog)
        self.credits_label.setObjectName(u"credits_label")
        self.credits_label.setGeometry(QRect(90, 85, 220, 40))
        self.credits_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(CreditsDialog)

        QMetaObject.connectSlotsByName(CreditsDialog)
    # setupUi

    def retranslateUi(self, CreditsDialog):
        CreditsDialog.setWindowTitle(QCoreApplication.translate("CreditsDialog", u"Credits", None))
        self.actionUser_Name_Generator.setText(QCoreApplication.translate("CreditsDialog", u"User Name Generator", None))
        self.actionPassword_Generator.setText(QCoreApplication.translate("CreditsDialog", u"Password Generator", None))
        self.actionPassword_Manager.setText(QCoreApplication.translate("CreditsDialog", u"Password Manager", None))
        self.credits_label.setText(QCoreApplication.translate("CreditsDialog", u"Developed by Doga Ege Ozden", None))
    # retranslateUi

