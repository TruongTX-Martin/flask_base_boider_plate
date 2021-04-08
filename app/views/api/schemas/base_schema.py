from marshmallow import INCLUDE, Schema, fields

from app.exceptions.parameter_error import ParameterError


class BaseSchema(Schema):
    pass

    def handle_error(self, exc, data, **kwargs):
        raise ParameterError(exc.messages, status_code=400)

    class Meta:
        unknown = INCLUDE
