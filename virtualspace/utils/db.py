# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import sqlalchemy as sa
from kivy.app import App
from sqlalchemy.orm import sessionmaker

from virtualspace import settings


def get_new_sa_session():
    engine = sa.create_engine(settings.DB_URL)
    session = sessionmaker(bind=engine)
    return session()


def get_app_sa_session():
    app = App.get_running_app()
    return app.sa_session
