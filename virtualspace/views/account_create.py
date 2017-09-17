# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

from virtualspace.controllers.account_create import AccountCreateController
from virtualspace.utils.views.base import BaseView


class AccountCreateView(BaseView):
    controller = AccountCreateController

    def init_labels(self):
        self.username_label = QLabel('Username')
        self.email_label = QLabel('Email')
        self.password_label = QLabel('Password')
        self.password_repeat_label = QLabel('Repeat password')

    def init_line_edits(self):
        self.username_line_edit = QLineEdit()
        self.email_line_edit = QLineEdit()
        self.password_line_edit = QLineEdit()
        self.password_repeat_line_edit = QLineEdit()

        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.password_repeat_line_edit.setEchoMode(QLineEdit.Password)

    def init_buttons(self):
        self.create_button = QPushButton('Create!')

    def connect_buttons(self):
        self.create_button.clicked.connect(self.__create_user)

    def init_layout(self):
        super(AccountCreateView, self).init_layout()
        self.layout.addWidget(self.username_label, 0, 0)
        self.layout.addWidget(self.email_label, 1, 0)
        self.layout.addWidget(self.password_label, 2, 0)
        self.layout.addWidget(self.username_line_edit, 0, 1)
        self.layout.addWidget(self.email_line_edit, 1, 1)
        self.layout.addWidget(self.password_line_edit, 2, 1)
        self.layout.addWidget(self.create_button, 3, 0)
        # self.layout.addWidget(self.password_repeat_label, 2, 0)
        # self.layout.addWidget(self.password_repeat_line_edit, 2, 1)

    def __create_user(self):
        username = self.username_line_edit.text()
        password = self.password_line_edit.text()
        email = self.email_line_edit.text()

        self.controller.create_account(self.sa_session, username, password, email)
