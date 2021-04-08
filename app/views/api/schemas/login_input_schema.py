from marshmallow import fields

from .base_schema import BaseSchema


class LoginInputSchema(BaseSchema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
