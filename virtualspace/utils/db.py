# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
import inspect

import sqlalchemy as sa
from kivy.app import App
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

from virtualspace import settings, models
from virtualspace.utils.models.bases import BaseModel


def get_new_sa_session():
    engine = sa.create_engine(settings.DB_URL)
    session = sessionmaker(bind=engine)
    return session()


def get_app_sa_session():
    app = App.get_running_app()
    return app.sa_session


def get_all_models_metadata():
    metadata = []

    for name, cls in inspect.getmembers(models):
        if inspect.isclass(cls) and issubclass(cls, BaseModel):
            metadata.append(cls.metadata)

    return metadata


def combine_metadata(*args):
    m = MetaData()
    for metadata in args:
        for t in metadata.tables.values():
            t.tometadata(m)
    return m
