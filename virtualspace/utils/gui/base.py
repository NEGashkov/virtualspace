# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import sqlalchemy as sa
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QWidget, QGridLayout

from virtualspace import settings


class BaseMainView(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BaseMainView, self).__init__(*args, **kwargs)

        self.init_ui()
        self.show()

    @property
    def sa_session(self):
        engine = sa.create_engine(settings.DB_URI, echo='debug')
        return sa.orm.sessionmaker(bind=engine)()

    def init_ui(self):
        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)


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
