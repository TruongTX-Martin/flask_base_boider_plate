from flask import Blueprint, Flask, redirect, request

from .controllers import me_controller, auth_controller, product_controller


def build_routes(app: Flask) -> None:
    app.register_blueprint(me_controller, url_prefix='/api/v1/me')
    app.register_blueprint(auth_controller, url_prefix='/api/v1/auth')
    app.register_blueprint(product_controller, url_prefix='/api/v1/product')
