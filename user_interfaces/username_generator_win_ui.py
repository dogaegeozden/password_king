# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'username_generator_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_UsernameGeneratorDialog(object):
    def setupUi(self, UsernameGeneratorDialog):
        if not UsernameGeneratorDialog.objectName():
            UsernameGeneratorDialog.setObjectName(u"UsernameGeneratorDialog")
        UsernameGeneratorDialog.resize(300, 350)
        self.include_numbers_checkbox = QCheckBox(UsernameGeneratorDialog)
        self.include_numbers_checkbox.setObjectName(u"include_numbers_checkbox")
        self.include_numbers_checkbox.setGeometry(QRect(235, 150, 15, 25))
        font = QFont()
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.include_numbers_checkbox.setFont(font)
        self.include_numbers_checkbox.setLayoutDirection(Qt.RightToLeft)
        self.include_numbers_checkbox.setStyleSheet(u"QAbstractButton {\n"
"	text-align: left;\n"
"}")
        self.include_numbers_checkbox.setChecked(True)
        self.capitalize_checkbox = QCheckBox(UsernameGeneratorDialog)
        self.capitalize_checkbox.setObjectName(u"capitalize_checkbox")
        self.capitalize_checkbox.setGeometry(QRect(235, 120, 15, 25))
        self.capitalize_checkbox.setLayoutDirection(Qt.RightToLeft)
        self.capitalize_checkbox.setStyleSheet(u"")
        self.capitalize_checkbox.setChecked(True)
        self.capitalize_label = QLabel(UsernameGeneratorDialog)
        self.capitalize_label.setObjectName(u"capitalize_label")
        self.capitalize_label.setGeometry(QRect(50, 120, 67, 25))
        self.include_numbers_label = QLabel(UsernameGeneratorDialog)
        self.include_numbers_label.setObjectName(u"include_numbers_label")
        self.include_numbers_label.setGeometry(QRect(50, 150, 121, 25))
        self.username_line_edit = QLineEdit(UsernameGeneratorDialog)
        self.username_line_edit.setObjectName(u"username_line_edit")
        self.username_line_edit.setGeometry(QRect(50, 50, 200, 25))
        self.generate_button = QPushButton(UsernameGeneratorDialog)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setGeometry(QRect(105, 200, 90, 25))
        self.save_button = QPushButton(UsernameGeneratorDialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(160, 285, 90, 25))
        self.cancel_button = QPushButton(UsernameGeneratorDialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(50, 285, 90, 25))

        self.retranslateUi(UsernameGeneratorDialog)

        QMetaObject.connectSlotsByName(UsernameGeneratorDialog)
    # setupUi

    def retranslateUi(self, UsernameGeneratorDialog):
        UsernameGeneratorDialog.setWindowTitle(QCoreApplication.translate("UsernameGeneratorDialog", u"Username Generator", None))
        self.include_numbers_checkbox.setText("")
        self.capitalize_checkbox.setText("")
        self.capitalize_label.setText(QCoreApplication.translate("UsernameGeneratorDialog", u"Capitalize", None))
        self.include_numbers_label.setText(QCoreApplication.translate("UsernameGeneratorDialog", u"Include Numbers", None))
        self.generate_button.setText(QCoreApplication.translate("UsernameGeneratorDialog", u"Generate", None))
        self.save_button.setText(QCoreApplication.translate("UsernameGeneratorDialog", u"Save", None))
        self.cancel_button.setText(QCoreApplication.translate("UsernameGeneratorDialog", u"Cancel", None))
    # retranslateUi

