import time
from typing import Dict, List, Optional

from flask import g, session
import ulid

from app.exceptions import APIResponseError, LogicError

from ..models import User
from ..repositories import UserRepository


class UserService(object):
    def __init__(self, user_repository: UserRepository, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_repository = user_repository

    def get_users(self, offset: int, limit: int) -> List[User]:
        return self.user_repository.get(offset, limit, User.id.desc())

    def get_user(self, id_: int) -> Optional[User]:
        return self.user_repository.find(id_)

    def create_user(self, fields: Dict) -> Optional[User]:
        user_fields = {
            'email': fields['email'],
            'password': fields['password'],
        }
        check_user = self.user_repository.get_user_by_email(fields['email'])
        if check_user is not None:
            raise APIResponseError('User already exist.')

        user = self.user_repository.create(user_fields)

        return user

    def update_user(self, id_: int, fields: Dict) -> Optional[User]:
        user_fields = {'email': fields['email']}

        user = self.user_repository.find(id_)
        if user is None:
            raise APIResponseError('User Not Found.')

        user = self.user_repository.update(user, user_fields)

        return user

    def create_anonymous_new_user(self) -> Optional[User]:
        user_fields = {
            'email': "",
            'password': "",
            'anonymous_id': ulid.new().str
        }
        user = self.user_repository.create(user_fields)
        return user

    def login_as_anonymous(self, anonymous_id: str) -> Optional[User]:
        user = self.user_repository.find_by_anonymous_id(anonymous_id)
        if user is None:
            raise APIResponseError('Incorrect User')

        return user

    def login(self, email: str, password: str) -> Optional[User]:

        user = self.user_repository.get_user_by_email(email)
        if user is None:
            raise APIResponseError('Incorrect username.')
        elif not user.check_password(password):
            raise APIResponseError('Incorrect password.')

        session.clear()
        session['user_id'] = user.id
        
        print('user login :', user.__dict__);
        return user

    def load_logged_in_user_to_request(self, user_id: str):
        if user_id is None:
            g.user = None
        else:
            g.user = self.user_repository.find(user_id)
