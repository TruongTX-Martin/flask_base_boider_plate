from flask import jsonify


class Status(object):
    def __init__(self, message: str = ""):
        self._message = message

    def response(self):
        return jsonify({"status": "success", "message": self._message})
