from flask import Flask

from .controllers import index_controller


def build_routes(app: Flask) -> None:
    app.register_blueprint(index_controller,
                           url_prefix='/',
                           template_folder='../../templates')
