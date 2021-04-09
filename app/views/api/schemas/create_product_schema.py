from marshmallow import fields

from .base_schema import BaseSchema


class CreateProductSchema(BaseSchema):
    name = fields.String(strict=True,required=True)
    description = fields.String(strict=True,required=True)
    image = fields.String(strict=True,required=True)
    old_price = fields.Integer(strict=True,required=True)
    new_price = fields.Integer(strict=True,required=True)