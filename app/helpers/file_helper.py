import json
import os
from pathlib import Path
import random
import string
import tempfile
import time

from app.config import Config

from .string_helper import StringHelper


class FileHelper(object):
    @classmethod
    def get_temporary_file(cls) -> Path:
        directory = tempfile.gettempdir()

        return Path(directory + '/' + "".join([
            random.choice(string.ascii_letters + string.digits)
            for i in range(12)
        ]) + "_" + str(int(time.time())) + ".tmp")

    @classmethod
    def create_name(cls):
        return StringHelper.random_string() + str(int(time.time()))

    @classmethod
    def poll_allowed_file(cls, filename):
        return '.' in filename and filename.rsplit(
            '.', 1)[1].lower() in Config.POLL_ALLOWED_EXTENSIONS

    @classmethod
    def get_assets(cls):

        if os.path.exists('static/asset-manifest.json'):
            with open('static/asset-manifest.json') as asset_file:
                try:
                    assets = json.load(asset_file)
                    return assets
                except:
                    return None

    @classmethod
    def get_thumbnail_youtube(cls, url):
        url = url.replace("https://www.youtube.com/embed/",
                          "https://img.youtube.com/vi/")
        return url + "/sddefault.jpg"
