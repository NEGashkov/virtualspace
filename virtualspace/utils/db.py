# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import sqlalchemy as sa

from virtualspace import settings


def get_sa_session():
    engine = sa.create_engine(settings.DB_URL)
    return sa.orm.sessionmaker(bind=engine)()
