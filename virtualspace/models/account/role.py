# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from gettext import gettext as _

import sqlalchemy as sa

from virtualspace.utils.models import BaseModel


class Role(BaseModel):
    __abstract__ = False

    title = sa.Column(sa.Unicode(128), info={'verbose_name': _('title')})
