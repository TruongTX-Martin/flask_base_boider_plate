from .base_entity import BaseEntity


class User(BaseEntity):
    def build_from_model(self):
        return {
            "anonymousId": self._model.anonymous_id,
            "id": self._model.id,
            "email": self._model.email,
            "name": self._model.name,
        }
