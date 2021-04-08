import datetime

from ..database import db


class UserRole(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column('id', db.BigInteger, primary_key=True)
    user_id = db.Column('user_id', db.BigInteger, nullable=False)
    role = db.Column('role', db.String(255), nullable=False)

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
