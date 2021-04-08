from flask import jsonify


class Error(object):
    def __init__(self, error: str):
        self._error = error

    def response(self):
        return jsonify({"status": "error", "message": self._error})
