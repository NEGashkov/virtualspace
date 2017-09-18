# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from virtualspace.utils.views.base import BaseMainWindow
from virtualspace.views.account import AccountCreateView
from virtualspace.views.login import LoginView
from virtualspace.views.menu import MenuView


class MainWindow(BaseMainWindow):
    def init_views(self):
        self.account_create_view = AccountCreateView()
        self.login_view = LoginView()
        self.menu_view = MenuView()

        self.views = (self.login_view, self.account_create_view, self.menu_view)
