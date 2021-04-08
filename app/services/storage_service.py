import mimetypes
import os
import tempfile
from typing import Dict

from werkzeug.utils import secure_filename

from app.config import Config
from app.helpers import FileHelper, StringHelper
from app.repositories.file_repository import FileRepository
from app.services.storage.local import Local as LocalStorage
from app.services.storage.s3 import S3 as S3Storage


class StorageService(object):
    def __init__(self, file_repository: FileRepository,
                 local_storage: LocalStorage, s3_storage: S3Storage, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.file_repository = file_repository
        self.storage_type = {'local': local_storage, 's3': s3_storage}
        self.storage = None

    def upload(self, file, additional: Dict = None):
        file_name = secure_filename(file.filename)
        file_path = os.path.join(tempfile.gettempdir() + file_name)
        file.save(os.path.join(file_path))
        new_file_name = FileHelper.create_name()
        file_key = new_file_name + "." + file_name.rsplit('.', 1)[1].lower()
        self.storage = self.storage_type[Config.STORAGE_TYPE]
        content_type = mimetypes.guess_type(
            file_path)[0] or 'application/octet-stream'
        file_url = self.storage.upload(file_path, file_key, content_type)
        file_fields = {
            'url': file_url,
            'media_type': content_type,
            'storage_type': Config.STORAGE_TYPE,
            'original_file_name': file_name
        }
        os.remove(file_path)
        return self.file_repository.create(file_fields)
