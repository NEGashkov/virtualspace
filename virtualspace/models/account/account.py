
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base, declared_attr

Base = declarative_base()

__all__ = ('Account',)


class Account(Base):

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    id = sa.Column(sa.Integer(), primary_key=True)


a = Account()
a.__class__.__name__.lower()