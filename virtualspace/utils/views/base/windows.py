# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import sqlalchemy as sa
from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from sqlalchemy.orm import sessionmaker

from virtualspace import settings


class BaseMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BaseMainWindow, self).__init__(*args, **kwargs)

        self.sa_session = self.get_sa_session()
        self.init_ui()
        self.show()

    def get_sa_session(self):
        engine = sa.create_engine(settings.DB_URL)
        return sa.orm.sessionmaker(bind=engine)()

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
