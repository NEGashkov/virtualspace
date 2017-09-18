# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from PyQt5.QtWidgets import QPushButton

from virtualspace.utils.views.base import BaseView


class MenuView(BaseView):
    grid = (
        ('list_button',),
        ('add_button',),
        ('settings_button',),
        ('logout_button',),
    )

    def init_buttons(self):
        self.list_button = QPushButton('List')
        self.add_button = QPushButton('Add')
        self.settings_button = QPushButton('Settings')
        self.logout_button = QPushButton('Logout')

    def connect_buttons(self):
        self.logout_button.clicked.connect(self.__logout)

    def __logout(self):
        self.stacked_widget.setCurrentWidget(self.main_window.login_view)
