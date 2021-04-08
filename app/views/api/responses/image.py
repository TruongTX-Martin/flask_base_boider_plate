from .base_entity import BaseEntity


class Image(BaseEntity):
    def build_from_model(self):
        return {
            "id": self._model.id,
            "originalFileName": self._model.original_file_name,
            "url": self._model.url,
        }
