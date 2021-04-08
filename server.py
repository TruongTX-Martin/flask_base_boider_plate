import logging

from app.bootstrap import create_app
from app.config import Config

app = create_app()

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == '__main__':
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)
