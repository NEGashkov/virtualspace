from gettext import gettext as _

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from virtualspace.models.base import BaseModel


class Product(BaseModel):
    __abstract__ = False

    number = sa.Column(sa.Unicode(16), nullable=False, info={'verbose_name': _('number')})
    registry_number = sa.Column(sa.Unicode(16), nullable=False, info={'verbose_name': _('number')})

    triplets = relationship('Triplet', backref='products')


class Unit(BaseModel):
    __abstract__ = False

    product_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('product.id'),
        info={'verbose_name': _('product')}
    )

    number = sa.Column(sa.Unicode(16), nullable=False, info={'verbose_name': _('number')})

    triplets = relationship('Triplet', backref='units')
    product = relationship('Product', backref='units')


class Subunit(BaseModel):
    __abstract__ = False

    unit_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('unit.id'),
        info={'verbose_name': _('unit')}
    )

    number = sa.Column(sa.Unicode(16), nullable=False, info={'verbose_name': _('number')})

    triplets = relationship('Triplet', backref='subunits')
    subunit = relationship('Unit', backref='subunits')


class Detail(BaseModel):
    __abstract__ = False

    subunit_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('subunit.id'),
        info={'verbose_name': _('subunit')}
    )

    number = sa.Column(sa.Unicode(16), nullable=False, info={'verbose_name': _('number')})

    triplets = relationship('Triplet', backref='details')
    units = relationship('Subunit', backref='details')
