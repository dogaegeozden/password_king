# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_a_new_safe_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreateNewSafeDialog(object):
    def setupUi(self, CreateNewSafeDialog):
        if not CreateNewSafeDialog.objectName():
            CreateNewSafeDialog.setObjectName(u"CreateNewSafeDialog")
        CreateNewSafeDialog.resize(400, 300)
        self.safe_name_line_edit = QLineEdit(CreateNewSafeDialog)
        self.safe_name_line_edit.setObjectName(u"safe_name_line_edit")
        self.safe_name_line_edit.setGeometry(QRect(100, 70, 200, 30))
        self.password_line_edit = QLineEdit(CreateNewSafeDialog)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setGeometry(QRect(100, 110, 200, 30))
        self.create_button = QPushButton(CreateNewSafeDialog)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setGeometry(QRect(150, 160, 90, 30))
        self.info_label = QLabel(CreateNewSafeDialog)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(31, 209, 340, 81))
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setWordWrap(True)

        self.retranslateUi(CreateNewSafeDialog)

        QMetaObject.connectSlotsByName(CreateNewSafeDialog)
    # setupUi

    def retranslateUi(self, CreateNewSafeDialog):
        CreateNewSafeDialog.setWindowTitle(QCoreApplication.translate("CreateNewSafeDialog", u"Create a New Safe", None))
        self.safe_name_line_edit.setPlaceholderText(QCoreApplication.translate("CreateNewSafeDialog", u"Safe Name...", None))
        self.password_line_edit.setPlaceholderText(QCoreApplication.translate("CreateNewSafeDialog", u"Password...", None))
        self.create_button.setText(QCoreApplication.translate("CreateNewSafeDialog", u"Create", None))
        self.info_label.setText("")
    # retranslateUi

