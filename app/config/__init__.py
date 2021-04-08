import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = str(Path(Path(__file__).parent.name + '/../.env').resolve())
default_local_storage_path = str(
    Path(Path(__file__).parent.name + 'app/static/uploads').resolve())
load_dotenv(dotenv_path)


class Config:
    NAME = os.getenv('NAME', 'Flask Sample')
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    DEBUG = True
    APP_HOST = os.getenv('APP_HOST', '127.0.0.1')
    APP_PORT = os.getenv('APP_PORT', '5000')
    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{password}@{host}:{port}/{name}'.format(
        **{
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', ''),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', '5432'),
            'name': os.getenv('DB_NAME', 'default_name'),
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STORAGE_TYPE = os.getenv('STORAGE_TYPE', 'local')
    POLL_ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

    AWS_KEY = os.getenv('AWS_KEY', '')
    AWS_SECRET = os.getenv('AWS_SECRET', '')
    STORAGE_S3_REGION = os.getenv('STORAGE_S3_REGION', '')
    STORAGE_S3_BUCKET_NAME = os.getenv('STORAGE_S3_BUCKET_NAME', '')

    MINIO_HOST = os.getenv('MINIO_HOST', '')
    MINIO_PORT = os.getenv('MINIO_PORT', '')
    MINIO_KEY = os.getenv('MINIO_KEY', '')
    MINIO_SECRET = os.getenv('MINIO_SECRET', '')
    STORAGE_MINIO_BUCKET_NAME = os.getenv('STORAGE_MINIO_BUCKET_NAME', '')

    STORAGE_LOCAL_DIRECTORY = os.getenv('STORAGE_LOCAL_DIRECTORY',
                                        default_local_storage_path)

    SESSION_TYPE = os.getenv('SESSION_TYPE')
    SESSION_FILE_DIR = os.getenv('SESSION_FILE_DIR')
    SESSION_FILE_THRESHOLD = int(os.getenv('SESSION_FILE_THRESHOLD'))
    TOKEN_EXPIRED_IN_DAYS = int(os.getenv('TOKEN_EXPIRED_IN_DAYS', 1))

