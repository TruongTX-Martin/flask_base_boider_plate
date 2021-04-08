import os
import shutil
from typing import Optional

from flask import request

from app.config import Config

from .base_storage import BaseStorage


class Local(BaseStorage):
    def upload(self,
               file_path: str,
               file_name: str = "",
               content_type: str = None) -> Optional[str]:

        shutil.copyfile(
            file_path, os.path.join(Config.STORAGE_LOCAL_DIRECTORY, file_name))
        return request.url_root + "static/uploads/" + file_name
