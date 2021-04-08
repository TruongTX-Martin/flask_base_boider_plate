from .base_entity import BaseEntity


class Token(BaseEntity):
    def build_from_model(self):
        return {
            "id": self._model.id,
            "email": self._model.email,
            "token": self._model.token,
            "anonymousId": self._model.anonymous_id
        }
