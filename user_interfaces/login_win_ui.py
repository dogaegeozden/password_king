# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(500, 500)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        LoginWindow.setFont(font)
        LoginWindow.setStyleSheet(u"")
        self.create_a_new_safe_action = QAction(LoginWindow)
        self.create_a_new_safe_action.setObjectName(u"create_a_new_safe_action")
        self.help_page_action = QAction(LoginWindow)
        self.help_page_action.setObjectName(u"help_page_action")
        self.credits_action = QAction(LoginWindow)
        self.credits_action.setObjectName(u"credits_action")
        self.central_widget = QWidget(LoginWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"#central_widget {\n"
"	background: #64ccff;\n"
"}")
        self.logo_label = QLabel(self.central_widget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(150, 30, 200, 200))
        self.logo_label.setPixmap(QPixmap(u":/logos/password_king_logo.png"))
        self.logo_label.setScaledContents(True)
        self.select_the_zip_file_button = QPushButton(self.central_widget)
        self.select_the_zip_file_button.setObjectName(u"select_the_zip_file_button")
        self.select_the_zip_file_button.setGeometry(QRect(165, 230, 170, 30))
        self.unlock_button = QPushButton(self.central_widget)
        self.unlock_button.setObjectName(u"unlock_button")
        self.unlock_button.setGeometry(QRect(200, 380, 90, 30))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.unlock_button.setFont(font1)
        self.unlock_button.setStyleSheet(u"#unlock_button {\n"
"	background: #d0ac4b;\n"
"	color: black;\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}")
        self.info_label = QLabel(self.central_widget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(50, 420, 400, 50))
        self.info_label.setStyleSheet(u"")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setWordWrap(True)
        self.zip_file_path_label = QLabel(self.central_widget)
        self.zip_file_path_label.setObjectName(u"zip_file_path_label")
        self.zip_file_path_label.setGeometry(QRect(10, 270, 480, 20))
        self.zip_file_path_label.setAlignment(Qt.AlignCenter)
        self.zip_file_path_label.setWordWrap(False)
        self.password_line_edit = QLineEdit(self.central_widget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setGeometry(QRect(165, 300, 170, 30))
        self.password_line_edit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.eye_button = QPushButton(self.central_widget)
        self.eye_button.setObjectName(u"eye_button")
        self.eye_button.setGeometry(QRect(340, 305, 20, 20))
        self.eye_button.setStyleSheet(u"#eye_button {\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/eye-half.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eye_button.setIcon(icon)
        LoginWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(LoginWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 500, 22))
        self.menu_help = QMenu(self.menu_bar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_safes = QMenu(self.menu_bar)
        self.menu_safes.setObjectName(u"menu_safes")
        LoginWindow.setMenuBar(self.menu_bar)

        self.menu_bar.addAction(self.menu_safes.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.help_page_action)
        self.menu_help.addAction(self.credits_action)
        self.menu_safes.addAction(self.create_a_new_safe_action)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Password King Unlock", None))
        self.create_a_new_safe_action.setText(QCoreApplication.translate("LoginWindow", u"Create a new safe", None))
        self.help_page_action.setText(QCoreApplication.translate("LoginWindow", u"Help page", None))
        self.credits_action.setText(QCoreApplication.translate("LoginWindow", u"Credits", None))
        self.logo_label.setText("")
        self.select_the_zip_file_button.setText(QCoreApplication.translate("LoginWindow", u"Select the zip file", None))
        self.unlock_button.setText(QCoreApplication.translate("LoginWindow", u"Unlock", None))
        self.info_label.setText("")
        self.zip_file_path_label.setText("")
        self.password_line_edit.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter your  password...", None))
        self.eye_button.setText("")
        self.menu_help.setTitle(QCoreApplication.translate("LoginWindow", u"Help", None))
        self.menu_safes.setTitle(QCoreApplication.translate("LoginWindow", u"Safes", None))
    # retranslateUi

