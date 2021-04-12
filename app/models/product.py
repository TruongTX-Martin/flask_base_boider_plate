import datetime
from sqlalchemy.dialects import sqlite
from ..database import db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column('id', db.BigInteger().with_variant(sqlite.INTEGER(), 'sqlite'), primary_key=True)
    name = db.Column('name', db.String(255),nullable=False)
    description = db.Column('description', db.String(255), nullable=False)
    image = db.Column('images', db.String(255), nullable=True)
    old_price = db.Column('old_price', db.BigInteger, nullable=True)
    is_delete = db.Column('is_delete', db.Boolean, nullable=True)
    new_price = db.Column('new_price', db.BigInteger, nullable=True)
    created_at = db.Column('created_at',
                           db.TIMESTAMP,
                           default=datetime.datetime.utcnow,
                           nullable=False)
    updated_at = db.Column('updated_at',
                           db.TIMESTAMP,
                           onupdate=datetime.datetime.utcnow,
                           default=datetime.datetime.utcnow,
                           nullable=False)

    def __repr__(self):
        return "<{name} '{id}'>".format(name=self.__class__.__name__,
                                        id=self.id)
