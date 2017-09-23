# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from virtualspace.utils.translation import gettext as _

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from virtualspace.utils.models.base import BaseModel


class ProductTriplet(BaseModel):
    __abstract__ = False

    product_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('product.id'),
        info={'verbose_name': _('product')}
    )
    triplet_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('triplet.id'),
        info={'verbose_name': _('triplet')}
    )

    product = relationship('Product', backref='triplets')
    triplet = relationship('Triplet', backref='products')


class UnitTriplet(BaseModel):
    __abstract__ = False

    unit_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('unit.id'),
        info={'verbose_name': _('unit')}
    )
    triplet_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('triplet.id'),
        info={'verbose_name': _('triplet')}
    )

    unit = relationship('Unit', backref='triplets')
    triplet = relationship('Triplet', backref='units')


class SubunitTriplet(BaseModel):
    __abstract__ = False

    subunit_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('subunit.id'),
        info={'verbose_name': _('subunit')}
    )
    triplet_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('triplet.id'),
        info={'verbose_name': _('triplet')}
    )

    subunit = relationship('Subunit', backref='triplets')
    triplet = relationship('Triplet', backref='subunits')


class DetailTriplet(BaseModel):
    __abstract__ = False

    detail_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('detail.id'),
        info={'verbose_name': _('detail')}
    )
    triplet_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('triplet.id'),
        info={'verbose_name': _('triplet')}
    )

    detail = relationship('Detail', backref='triplets')
    triplet = relationship('Triplet', backref='details')
