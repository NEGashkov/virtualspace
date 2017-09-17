# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from PyQt5.QtWidgets import QWidget, QGridLayout


class BaseView(QWidget):
    controller = None

    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.init_widgets()
        self.connect_buttons()
        self.init_layout()

    def init_widgets(self):
        self.init_labels()
        self.init_line_edits()
        self.init_buttons()

    def init_labels(self):
        pass

    def init_line_edits(self):
        pass

    def init_buttons(self):
        pass

    def connect_buttons(self):
        pass

    def init_layout(self):
        self.layout = QGridLayout(self)

    @property
    def stacked_widget(self):
        return self.parentWidget()

    @property
    def main_window(self):
        return self.stacked_widget.parentWidget()

    @property
    def sa_session(self):
        return self.main_window.sa_session
