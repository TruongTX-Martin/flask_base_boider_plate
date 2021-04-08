from datetime import datetime, timedelta
from typing import Optional

from flask_login import UserMixin
import jwt
from sqlalchemy import event
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash, generate_password_hash

from app.config import Config

from ..database import db
from ..helpers import SessionHelper


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.BigInteger, primary_key=True)
    email = db.Column('email', db.String(255), nullable=False)
    password = db.Column('password', db.String(255), nullable=False)
    anonymous_id = db.Column('anonymous_id', db.String(255), nullable=True)
    created_at = db.Column('created_at',
                           db.TIMESTAMP,
                           default=datetime.utcnow,
                           nullable=False)
    updated_at = db.Column('updated_at',
                           db.TIMESTAMP,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow,
                           nullable=False)

    def __repr__(self):
        return "<{name} '{id}'>".format(name=self.__class__.__name__,
                                        id=self.id)

    @staticmethod
    def is_authenticated() -> bool:
        return True

    @staticmethod
    def is_active() -> bool:
        return True

    @staticmethod
    def is_anonymous(self) -> bool:
        return False

    def get_id(self) -> int:
        return self.id

    def check_password(self, password):
        password = password.strip()
        if not password:
            return False
        return check_password_hash(self.password, password)

    @hybrid_property
    def token(self):
        exp = datetime.utcnow() + timedelta(days=Config.TOKEN_EXPIRED_IN_DAYS)
        encoded = jwt.encode({
            'id': self.id,
            'exp': exp
        },
                             Config.SECRET_KEY,
                             algorithm='HS256')
        return encoded.decode('utf-8')

    def __repr__(self):
        return "<User '{}'>".format(self.id)


def encrypt_password(target, value, old_value, initiator):
    if value is None or value == '':
        return ''
    return generate_password_hash(value)


event.listen(User.password, 'set', encrypt_password, retval=True)

login_manager = SessionHelper.get_login_manager()


@login_manager.user_loader
def user_loader(user_id: int) -> Optional[User]:
    return User.query.filter_by(id=user_id).first()
