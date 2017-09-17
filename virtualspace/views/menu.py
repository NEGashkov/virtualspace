# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from PyQt5.QtWidgets import QPushButton

from virtualspace.utils.views.base import BaseView


class MenuView(BaseView):
    # controller = MenuController

    def init_buttons(self):
        self.list_button = QPushButton('List')
        self.add_button = QPushButton('Add')
        self.settings_button = QPushButton('Settings')
        self.logout_button = QPushButton('Logout')

    def connect_buttons(self):
        self.logout_button.clicked.connect(self.__logout)

    def init_layout(self):
        super(MenuView, self).init_layout()

        self.layout.addWidget(self.list_button, 0, 0, 1, 1)
        self.layout.addWidget(self.add_button, 1, 0)
        self.layout.addWidget(self.settings_button, 1, 1)
        self.layout.addWidget(self.logout_button, 2, 0)

    def __logout(self):
        # Use controller.
        self.stacked_widget.setCurrentWidget(self.main_window.login_view)
