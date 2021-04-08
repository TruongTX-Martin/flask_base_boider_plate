from functools import wraps

from flask import Flask, jsonify, make_response, request
from injector import inject
import jwt

from app.config import Config
from app.exceptions import AuthenticationError
from app.services import UserService


@inject
def token_required(func):
    @wraps(func)
    @inject
    def decorator(user_service: UserService, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            raise AuthenticationError('Unauthorized - Token not found')

        try:
            _, token = auth_header.split()
        except ValueError:
            raise AuthenticationError('Unauthorized - Token is not valid')

        if token is None:
            raise AuthenticationError('Unauthorized - Token is not valid')

        try:
            decoded = jwt.decode(token, Config.SECRET_KEY, algorithms='HS256')
        except jwt.DecodeError as e:
            raise AuthenticationError(
                'Unauthorized - Token is not valid. {}'.format(e))
        except jwt.ExpiredSignatureError as e:
            raise AuthenticationError(
                'Unauthorized - Token is expired. {}'.format(e))
        except Exception as e:
            raise AuthenticationError(
                'Unauthorized - Something went wrong. {}'.format(e))
        user_service.load_logged_in_user_to_request(decoded['id'])
        return func(*args, **kwargs)

    return decorator
