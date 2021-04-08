from typing import Any

from flask import jsonify

from ....database import db


class BaseEntity(object):
    def __init__(self, model: db.Model, additional_data=None):
        self._model = model
        self._additional_data = additional_data
        if type(additional_data) is dict:
            self._additional_data = additional_data
        else:
            self._additional_data = {}

    def build_from_model(self):
        return {"id": self._model.id}

    def response(self):
        return jsonify(self.build_from_model())

    def _get(self, key: str, default=None) -> Any:
        if key in self._additional_data:
            return self._additional_data[key]
        return default
