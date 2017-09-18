# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from PyQt5 import Qt

from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QApplication, QMessageBox

from virtualspace.controllers.login import LoginController
from virtualspace.utils.views.base import BaseView


class LoginView(BaseView):
    controller = LoginController

    grid = (
        (None, 'title_label', None),
        ('username_label', 'username_line_edit', None),
        ('password_label', 'password_line_edit', None),
        ('login_button', 'create_account_button', 'exit_button'),
        (None, 'version_label', None),
    )

    def init_labels(self):
        self.title_label = QLabel('Login to Virtual Space')
        self.version_label = QLabel('Version 0.1a1')
        self.username_label = QLabel('Username')
        self.password_label = QLabel('Password')

        self.title_label.setAlignment(Qt.Qt.AlignCenter)
        self.version_label.setAlignment(Qt.Qt.AlignCenter)

    def init_line_edits(self):
        self.username_line_edit = QLineEdit()
        self.password_line_edit = QLineEdit()

        self.password_line_edit.setEchoMode(QLineEdit.Password)

    def init_buttons(self):
        self.login_button = QPushButton('Login')
        self.create_account_button = QPushButton('Create new account')
        self.exit_button = QPushButton('Exit')

    def connect_buttons(self):
        self.login_button.clicked.connect(self.__login)
        self.create_account_button.clicked.connect(self.__create_account)
        self.exit_button.clicked.connect(self.__exit)

    def __login(self):
        username = self.username_line_edit.text()
        password = self.password_line_edit.text()

        success = self.controller.do_login(self.sa_session, username, password)

        if success:
            self.stacked_widget.setCurrentWidget(self.main_window.menu_view)
        else:
            QMessageBox.warning(self, 'Error', 'Its not okay!', QMessageBox.Ok)

    def __create_account(self):
        self.stacked_widget.setCurrentWidget(self.main_window.account_create_view)

    def __exit(self):
        QApplication.quit()
