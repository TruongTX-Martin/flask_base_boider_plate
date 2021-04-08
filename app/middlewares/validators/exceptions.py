import json
from ...exceptions.api_response_error import APIResponseError


class UndefinedParamType(APIResponseError):
    """
    Not allowed type of param(GET, POST )
    """


class NotAllowedType(APIResponseError):
    """
    Not allowed type. See: rules.ALLOWED_TYPES
    """


class InvalidRequest(APIResponseError):
    status_code = 401