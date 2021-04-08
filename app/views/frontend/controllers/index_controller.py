import os.path

from flask import (Blueprint, Flask, render_template, request, send_file,
                   url_for)

from app.config import Config

app = Blueprint('frontend.index', __name__)


@app.route('/')
def index():
    title = Config.NAME
    meta_data = {'title': title}

    return render_template('pages/index.html',
                           title=title,
                           meta_data=meta_data)


@app.route('/static/uploads/<file_name>')
def file(file_name: str):
    return send_file(os.path.join(Config.STORAGE_LOCAL_DIRECTORY, file_name))
