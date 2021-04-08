import base64
from functools import wraps

from flask import Response, request

from app.config import Config


def check(authorization_header):
    encoded = authorization_header.split()[-1]
    auth = Config.BASIC_AUTH_USER + ":" + Config.BASIC_AUTH_PASSWORD
    if encoded == base64.b64encode(auth.encode("utf-8")).decode("utf-8"):
        return True


def basic_auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            authorization_header = request.headers.get('Authorization')
            if authorization_header and check(authorization_header):
                return f(*args, **kwargs)
            else:
                resp = Response()
                resp.headers['WWW-Authenticate'] = 'Basic'
                return resp, 401
        except Exception as e:
            raise e

    return decorated
