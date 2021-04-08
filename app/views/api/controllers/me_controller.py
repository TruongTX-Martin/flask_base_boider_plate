from flask import Blueprint, redirect, request
from flask import Blueprint, current_app, g, request
from injector import inject

from ....exceptions import LogicError, NotFoundError, ParameterError
from ....middlewares.authenticate import token_required
from ..responses import Error, User

app = Blueprint('api.me', __name__)


@app.route('', methods=["GET"])
@inject
@token_required
def me():
    user = g.user
    return User(model=user).response(), 200
