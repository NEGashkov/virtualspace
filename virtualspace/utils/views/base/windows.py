# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from virtualspace.utils.db import get_sa_session
from virtualspace.utils.gui import center_window_on_screen


class BaseMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BaseMainWindow, self).__init__(*args, **kwargs)

        self.sa_session = get_sa_session()
        self.init_ui()
        self.setup_window()

    def init_ui(self):
        self.init_views()
        self.init_central_widget()

    def init_views(self):
        self.views = ()

    def init_central_widget(self):
        self.central_widget = QStackedWidget(self)

        for view in self.views:
            self.central_widget.addWidget(view)

        self.setCentralWidget(self.central_widget)

    def setup_window(self):
        self.setFixedSize(800, 400)
        self.setWindowTitle('Virtual Space')
        self.center()
        self.show()

    def center(self):
        center_window_on_screen(self)
