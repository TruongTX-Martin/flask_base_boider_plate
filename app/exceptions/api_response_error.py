from .base_exception import BaseException


class APIResponseError(BaseException):

    status_code = 400

    def __init__(self, error, status_code=None, payload=None):
        Exception.__init__(self)
        self._error = error
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        return_value = dict(self.payload or ())
        return_value['status'] = 'error'
        return_value['message'] = self._error
        return return_value
