from .exceptions import (
    NotAllowedType,
    UndefinedParamType,
    InvalidRequest
)

PARAM_TYPES = ('GET', 'PATH', 'JSON', 'FORM')
ALLOWED_TYPES = (str, bool, int, float, dict, list)

class Param(object):

    def __init__(self, name, param_type, value_type=None,
                 required=True, default=None, rules=None):
        """
        :param mixed default:
        :param bool required:
        :param type value_type: type of value (int, list, etc)
        :param list|CompositeRule rules:
        :param str name: name of param
        :param str param_type: type of request param (see: PARAM_TYPES)
        :raises: UndefinedParamType, NotAllowedType
        """

        if param_type not in PARAM_TYPES:
            raise UndefinedParamType('Undefined param type "%s"' % param_type)

        if value_type and value_type not in ALLOWED_TYPES:
            raise NotAllowedType('Value type "%s" is not allowed' % value_type)

        self.value_type = value_type
        self.default = default
        self.required = required
        self.name = name
        self.param_type = param_type
        self.rules = rules or []

    def value_to_type(self, value):
        """
        :param mixed value:
        :return: mixed
        """
        if self.param_type != 'JSON':
            if self.value_type == bool:
                low_val = value.lower()

                if low_val in ('true', '1'):
                    value = True
                elif low_val in ('false', '0'):
                    value = False
            elif self.value_type == list:
                value = [item.strip() for item in value.split(',')]
            elif self.value_type == dict:
                value = {
                    item.split(':')[0].strip(): item.partition(':')[-1].strip()
                    for item in value.split(',')
                }

        if self.value_type:
            value = self.value_type(value)

        return value
