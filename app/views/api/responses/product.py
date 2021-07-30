from .base_entity import BaseEntity

class Product(BaseEntity):
    def build_from_model(self):
        return {
            "id": self._model.id,
            "name": self._model.name,
            "description": self._model.description,
            "image": self._model.image,
            "old_price": self._model.old_price,
            "new_price": self._model.new_price,
            "update": "Test3"
        }