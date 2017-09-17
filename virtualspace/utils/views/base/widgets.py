# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from PyQt5.QtWidgets import QWidget, QGridLayout


class BaseWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(BaseWidget, self).__init__(*args, **kwargs)

        self.init_ui()

    @property
    def stacked_widget(self):
        return self.parentWidget()

    @property
    def main_window(self):
        return self.stacked_widget.parentWidget()

    @property
    def sa_session(self):
        return self.main_window.sa_session

    def init_ui(self):
        self.layout = QGridLayout(self)
