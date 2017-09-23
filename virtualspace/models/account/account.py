# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from virtualspace.utils.translation import gettext as _

import sqlalchemy as sa
from sqlalchemy.orm import relationship, validates

from virtualspace.utils.models.base import BaseModel
from virtualspace.validators.account import AccountValidator


class Account(BaseModel):
    __abstract__ = False

    role_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('role.id'),
        info={'verbose_name': _('role')}
    )

    is_active = sa.Column(sa.Boolean, nullable=False, default=True, info={'verbose_name': _('is active')})

    username = sa.Column(sa.Unicode(128), unique=True, nullable=False, info={'verbose_name': _('username')})
    email = sa.Column(sa.Unicode(128), unique=True, nullable=False, info={'verbose_name': _('email')})
    password = sa.Column(sa.Unicode(128), nullable=False, info={'verbose_name': _('password')})

    first_name = sa.Column(sa.Unicode(128), info={'verbose_name': _('first name')})
    patr_name = sa.Column(sa.Unicode(128), info={'verbose_name': _('patr name')})
    last_name = sa.Column(sa.Unicode(128), info={'verbose_name': _('last name')})

    role = relationship('Role', backref='accounts')

    validator = AccountValidator

    def __str__(self):
        return '<User: {username}>'.format(username=self.username)

    @validates('username', include_removes=True)
    def validate_username(self, key, value, is_remove):
        return self.validator.validate_username(key, value, is_remove)
