from gettext import gettext as _

import sqlalchemy as sa

from virtualspace.models.base import BaseModel


class Role(BaseModel):
    __abstract__ = False

    title = sa.Column(sa.Unicode(128), info={'verbose_name': _('title')})
