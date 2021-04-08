from .api_response_error import APIResponseError


class AuthenticationError(APIResponseError):
    status_code = 401
