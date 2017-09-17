# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import sqlalchemy as sa
from PyQt5.QtWidgets import QMainWindow, QStackedWidget

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
