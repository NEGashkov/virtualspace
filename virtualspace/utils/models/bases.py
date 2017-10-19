# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

"""Base models for application.

This module contains very base and generic models for inheritance in the
future.

"""
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from virtualspace.utils.translation import gettext as _

SqlAlchemyBase = declarative_base()


class BaseModel(SqlAlchemyBase):
    """Generic base model to inherit models from.

    There is declared very generic attributes such as table name and primary
    key for an entry.

    Class vars:
        __abstract__ (bool): Whether or not table will be generated for this
            model in database schema.

    """
    __abstract__ = True

    def __repr__(self):
        return '<{cls}: {id}>'.format(cls=self.__class__.__name__, id=self.id)

    @declared_attr
    def __tablename__(self):
        """Name of a table in database schema.

        `__tablename__` is taken by SQLAlchemy to create table in database.
        Table name is generated by lowercasing model's name.

        Returns:
            str: Model's name that will become table's name stored in database.

        """
        return self.__name__.lower()

    id = sa.Column(sa.Integer, primary_key=True, info={'verbose_name': _('id')})
