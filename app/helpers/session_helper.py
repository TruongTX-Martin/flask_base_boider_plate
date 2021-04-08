from flask_login import LoginManager

from ..session import login_manager


class SessionHelper(object):
    @classmethod
    def get_login_manager(cls) -> LoginManager:
        return login_manager
