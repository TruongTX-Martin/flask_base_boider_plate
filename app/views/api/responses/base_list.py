from typing import List

from flask import jsonify

from ....database import db
from .base_entity import BaseEntity


class BaseList(object):
    _target = BaseEntity

    def __init__(self,
                 models: List[db.Model],
                 total_count: int = 0,
                 offset: int = 0,
                 limit: int = 0):
        self._models = models
        self._total_count = total_count
        self._offset = offset
        self._limit = limit

    def build_from_models(self):
        lists = [
            self._target(model).build_from_model() for model in self._models
        ]
        return {
            "list": lists,
            "totalCount": self._total_count,
            "offset": self._offset,
            "limit": self._limit
        }

    def response(self):
        return jsonify(self.build_from_models())
