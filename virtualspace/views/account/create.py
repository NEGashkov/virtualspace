# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

from virtualspace.controllers.account import AccountCreateController
from virtualspace.utils.views.base import BaseView


class AccountCreateView(BaseView):
    controller = AccountCreateController

    grid = (
        ('username_label', 'username_line_edit', 'username_error_label'),
        ('email_label', 'email_line_edit', 'email_error_label'),
        ('password_label', 'password_line_edit', 'password_error_label'),
        ('password_repeat_label', 'password_repeat_line_edit', 'password_repeat_error_label'),
        (None, 'create_button', 'back_button'),
    )

    def init_labels(self):
        self.username_label = QLabel('Username')
        self.email_label = QLabel('Email')
        self.password_label = QLabel('Password')
        self.password_repeat_label = QLabel('Repeat password')

        self.username_error_label = QLabel()
        self.email_error_label = QLabel()
        self.password_error_label = QLabel()
        self.password_repeat_error_label = QLabel()

    def init_line_edits(self):
        self.username_line_edit = QLineEdit()
        self.email_line_edit = QLineEdit()
        self.password_line_edit = QLineEdit()
        self.password_repeat_line_edit = QLineEdit()

        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.password_repeat_line_edit.setEchoMode(QLineEdit.Password)

    def init_buttons(self):
        self.create_button = QPushButton('Create!')
        self.back_button = QPushButton('Back')

    def connect_buttons(self):
        self.create_button.clicked.connect(self.__create_user)
        self.back_button.clicked.connect(self.__back)

    def __create_user(self):
        username = self.username_line_edit.text()
        password = self.password_line_edit.text()
        email = self.email_line_edit.text()

        self.controller.create_account(self.sa_session, username, password, email)

    def __back(self):
        self.stacked_widget.setCurrentWidget(self.main_window.login_view)
