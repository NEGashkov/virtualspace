# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from PyQt5 import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QApplication, QMessageBox
from sqlalchemy import exists

from virtualspace.models import Account
from virtualspace.utils.gui import BaseMainView, BaseWidget


class MainWindow(BaseMainView):
    def init_ui(self):
        super(MainWindow, self).init_ui()

        login_widget = LoginWidget()
        self.central_widget.addWidget(login_widget)


class LoginWidget(BaseWidget):
    def init_ui(self):
        super(LoginWidget, self).init_ui()

        login_to_vs_label = QLabel('Login to VS')
        version_label = QLabel('version 0.0.1.a1')

        login_to_vs_label.setAlignment(Qt.Qt.AlignCenter)
        version_label.setAlignment(Qt.Qt.AlignCenter)

        nickname_label = QLabel('nickname')
        password_label = QLabel('password')

        self.nickname_line_edit = QLineEdit()
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        login_button = QPushButton('Login')
        exit_button = QPushButton('Exit')

        login_button.clicked.connect(self.__login)
        exit_button.clicked.connect(self.__exit)

        self.layout.addWidget(login_to_vs_label, 0, 0, 1, 1)
        self.layout.addWidget(nickname_label, 1, 0)
        self.layout.addWidget(self.nickname_line_edit, 1, 1)
        self.layout.addWidget(password_label, 2, 0)
        self.layout.addWidget(self.password_line_edit, 2, 1)
        self.layout.addWidget(login_button, 3, 0)
        self.layout.addWidget(exit_button, 3, 1)
        self.layout.addWidget(version_label, 4, 0, 4, 1)

    def __exit(self):
        QApplication.quit()

    def __login(self):
        menu_widget = MenuWidget()

        nickname = self.nickname_line_edit.text()
        password = self.password_line_edit.text()

        success = self.sa_session.query(exists().where(Account.username == nickname and Account.password == password)).scalar()

        if success:
            QMessageBox.warning(self, 'OK', 'Its ok!', QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Error', 'Its not okay!', QMessageBox.Ok)

        self.stacked_widget.addWidget(menu_widget)
        self.stacked_widget.setCurrentWidget(menu_widget)


class MenuWidget(BaseWidget):
    def init_ui(self):
        super(MenuWidget, self).init_ui()

        list_button = QPushButton('Menu')
        add_button = QPushButton('Menu')
        settings_button = QPushButton('Menu')
        logout_button = QPushButton('Logout')

        logout_button.clicked.connect(self.__log_out)

        self.layout.addWidget(list_button, 0, 0, 1, 1)
        self.layout.addWidget(add_button, 1, 0)
        self.layout.addWidget(settings_button, 1, 1)
        self.layout.addWidget(logout_button, 2, 0)

    def __log_out(self):
        logout_widget = LoginWidget()
        self.stacked_widget.addWidget(logout_widget)
        self.stacked_widget.setCurrentWidget(logout_widget)
