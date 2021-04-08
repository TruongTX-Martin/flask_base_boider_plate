from typing import Optional

import boto3

from app.config import Config

from .base_storage import BaseStorage


class S3(BaseStorage):
    bucket_name = Config.STORAGE_S3_BUCKET_NAME
    storage_type = Config.STORAGE_TYPE

    def upload(self,
               file_path: str,
               file_name: str = "",
               content_type: str = "") -> Optional[str]:

        s3 = self.get_client()
        s3.upload_file(file_path,
                       self.bucket_name,
                       file_name,
                       ExtraArgs={
                           'ACL': 'public-read',
                           'ContentType': content_type
                       })
        return self.get_file(file_name)

    def get_client(self):
        s3 = boto3.client('s3',
                          Config.STORAGE_S3_REGION,
                          aws_access_key_id=Config.AWS_KEY,
                          aws_secret_access_key=Config.AWS_SECRET)
        return s3

    def get_file(self, file_key):
        s3 = self.get_client()
        bucket_location = s3.get_bucket_location(Bucket=self.bucket_name)
        object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
            bucket_location['LocationConstraint'], self.bucket_name, file_key)
        return object_url
