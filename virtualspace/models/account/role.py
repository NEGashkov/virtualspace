# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import sqlalchemy as sa

from virtualspace.utils.models.bases import BaseModel
from virtualspace.utils.translation import gettext as _


class Role(BaseModel):
    __abstract__ = False

    title = sa.Column(sa.Unicode(128), info={'verbose_name': _('title')})
