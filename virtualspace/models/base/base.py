# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

"""Base models for application.

This module contains very base and generic models for inheritance in the
future. This models allows creation models and its versions.

"""

from gettext import gettext as _

import sqlalchemy as sa
from sqlalchemy.ext.declarative import as_declarative

from virtualspace.models.base.mixins import BaseModelMixin


@as_declarative()
class Base(BaseModelMixin):

    @property
    def versions(self):
        """Link to origin's versions.
        
        Relationship to versions which this model refers to. Rewrite versions
        like this:
        
            versions = relationship('BaseVersion', back_populates='origin')
        
        Raises:
            NotImplementedError: Occurs when class inherited this base class
                and did not define versions model.
        
        """
        raise NotImplementedError('Define versions model for this model.')


@as_declarative()
class BaseVersion(BaseModelMixin):

    @property
    def origin_id(self):
        """Record in table to version's origin.
        
        Foreign key to origin which this version refers to. Rewrite origin_id
        like this:
        
            origin_id = sa.Column(
                sa.Integer,
                sa.ForeignKey('base.id'),
                info={'verbose_name': _('origin')}
            )
        
        Raises:
            NotImplementedError: Occurs when class inherited this base class
                and did not define origin model which it refers to.
        
        """
        raise NotImplementedError('Define origin for this version model.')

    @property
    def origin(self):
        """Link to version's origin.
        
        Relationship to origin which this version refers to. Rewrite origin
        like this:
        
            origin = relationship('Base', back_populates='versions')
        
        Raises:
            NotImplementedError: Occurs when class inherited this base class
                and not defined origin model which it refers to.
        
        """
        raise NotImplementedError('Define origin for this version model.')

    reason = sa.Column(sa.Unicode(length=32), info={'verbose_name': _('reason of change')})
