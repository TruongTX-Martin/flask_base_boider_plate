from flask import Blueprint, current_app, g, request
from injector import inject

from app.services import UserService
from app.views.api.schemas import LoginInputSchema

from ..responses import Error, Token, User
from ....middlewares.request_validate import *

app = Blueprint('api.auth', __name__)


@app.route("/signin", methods=["POST"])
@inject
@request_validate(
    Param('email', 'JSON', str, rules=[Email()]),
    Param('password', 'JSON', str, rules=[MinLength(6)])
)
def signin(user_service: UserService):
    request_data = request.get_json()
    LoginInputSchema().load(request_data)
    input_data = {
        'email': request_data['email'],
        'password': request_data['password']
    }
    user = user_service.login(**input_data)
    return Token(user).response()


@app.route("/signup", methods=["POST"])
@inject
@request_validate(
    Param('email', 'JSON', str, rules=[Email()]),
    Param('password', 'JSON', str, rules=[MinLength(6)])
)
def signup(user_service: UserService):
    request_data = request.get_json()
    LoginInputSchema().load(request_data)
    input_data = {
        'email': request_data['email'],
        'password': request_data['password']
    }

    user = user_service.create_user(input_data)
    print('Sign up create user:', user.__dict__);
    return User(user).response()