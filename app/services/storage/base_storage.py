from typing import Optional


class BaseStorage(object):
    def upload(self,
               file_path: str,
               file_name: str = "",
               content_type: str = None) -> Optional[str]:
        pass

    def get_client(self):
        pass

    def get_file(self, file_key):
        pass
