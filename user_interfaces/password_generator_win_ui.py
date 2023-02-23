# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_generator_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PasswordGeneratorDialog(object):
    def setupUi(self, PasswordGeneratorDialog):
        if not PasswordGeneratorDialog.objectName():
            PasswordGeneratorDialog.setObjectName(u"PasswordGeneratorDialog")
        PasswordGeneratorDialog.resize(320, 500)
        PasswordGeneratorDialog.setStyleSheet(u"#centralwidget {\n"
"}")
        self.actionUser_Name_Generator = QAction(PasswordGeneratorDialog)
        self.actionUser_Name_Generator.setObjectName(u"actionUser_Name_Generator")
        self.actionPassword_Generator = QAction(PasswordGeneratorDialog)
        self.actionPassword_Generator.setObjectName(u"actionPassword_Generator")
        self.actionPassword_Manager = QAction(PasswordGeneratorDialog)
        self.actionPassword_Manager.setObjectName(u"actionPassword_Manager")
        self.central_widget = QWidget(PasswordGeneratorDialog)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setGeometry(QRect(0, -10, 320, 501))
        self.generate_button = QPushButton(self.central_widget)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setGeometry(QRect(110, 310, 100, 25))
        self.generate_button.setStyleSheet(u"")
        self.small_letters_spin_box = QSpinBox(self.central_widget)
        self.small_letters_spin_box.setObjectName(u"small_letters_spin_box")
        self.small_letters_spin_box.setGeometry(QRect(230, 130, 50, 30))
        self.small_letters_spin_box.setMaximum(20)
        self.small_letters_spin_box.setValue(5)
        self.small_letters_label = QLabel(self.central_widget)
        self.small_letters_label.setObjectName(u"small_letters_label")
        self.small_letters_label.setGeometry(QRect(30, 130, 150, 30))
        self.capital_letters_label = QLabel(self.central_widget)
        self.capital_letters_label.setObjectName(u"capital_letters_label")
        self.capital_letters_label.setGeometry(QRect(30, 170, 150, 30))
        self.capital_letters_spin_box = QSpinBox(self.central_widget)
        self.capital_letters_spin_box.setObjectName(u"capital_letters_spin_box")
        self.capital_letters_spin_box.setGeometry(QRect(230, 170, 50, 30))
        self.capital_letters_spin_box.setValue(5)
        self.numbers_spin_box = QSpinBox(self.central_widget)
        self.numbers_spin_box.setObjectName(u"numbers_spin_box")
        self.numbers_spin_box.setGeometry(QRect(230, 210, 50, 30))
        self.numbers_spin_box.setValue(5)
        self.numbers_label = QLabel(self.central_widget)
        self.numbers_label.setObjectName(u"numbers_label")
        self.numbers_label.setGeometry(QRect(30, 210, 150, 30))
        self.symbols_label = QLabel(self.central_widget)
        self.symbols_label.setObjectName(u"symbols_label")
        self.symbols_label.setGeometry(QRect(30, 250, 150, 30))
        self.symbols_spin_box = QSpinBox(self.central_widget)
        self.symbols_spin_box.setObjectName(u"symbols_spin_box")
        self.symbols_spin_box.setGeometry(QRect(230, 250, 50, 30))
        self.symbols_spin_box.setValue(5)
        self.password_line_edit = QLineEdit(self.central_widget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setGeometry(QRect(60, 70, 200, 30))
        self.save_button = QPushButton(self.central_widget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(165, 400, 90, 25))
        self.cancel_button = QPushButton(self.central_widget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(55, 400, 90, 25))

        self.retranslateUi(PasswordGeneratorDialog)

        QMetaObject.connectSlotsByName(PasswordGeneratorDialog)
    # setupUi

    def retranslateUi(self, PasswordGeneratorDialog):
        PasswordGeneratorDialog.setWindowTitle(QCoreApplication.translate("PasswordGeneratorDialog", u"Password Generator", None))
        self.actionUser_Name_Generator.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"User Name Generator", None))
        self.actionPassword_Generator.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Password Generator", None))
        self.actionPassword_Manager.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Password Manager", None))
        self.generate_button.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Generate", None))
        self.small_letters_label.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Small Letters", None))
        self.capital_letters_label.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Capital Letters", None))
        self.numbers_label.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Numbers", None))
        self.symbols_label.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Symbols", None))
        self.save_button.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Save", None))
        self.cancel_button.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Cancel", None))
    # retranslateUi

