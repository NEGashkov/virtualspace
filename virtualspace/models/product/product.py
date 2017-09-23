# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from virtualspace.utils.translation import gettext as _

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from virtualspace.utils.models.base import BaseModel


class Product(BaseModel):
    __abstract__ = False

    number = sa.Column(sa.Unicode(16), nullable=False, info={'verbose_name': _('number')})
    registry_number = sa.Column(sa.Unicode(16), nullable=False, info={'verbose_name': _('number')})


class Unit(BaseModel):
    __abstract__ = False

    product_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('product.id'),
        info={'verbose_name': _('product')}
    )

    number = sa.Column(sa.Unicode(16), nullable=False, info={'verbose_name': _('number')})

    product = relationship('Product', backref='units')


class Subunit(BaseModel):
    __abstract__ = False

    unit_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('unit.id'),
        info={'verbose_name': _('unit')}
    )

    number = sa.Column(sa.Unicode(16), nullable=False, info={'verbose_name': _('number')})

    unit = relationship('Unit', backref='subunits')


class Detail(BaseModel):
    __abstract__ = False

    subunit_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('subunit.id'),
        info={'verbose_name': _('subunit')}
    )

    number = sa.Column(sa.Unicode(16), nullable=False, info={'verbose_name': _('number')})

    subunit = relationship('Subunit', backref='details')
