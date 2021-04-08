from flask import Flask, jsonify

from app.exceptions.api_response_error import APIResponseError


class ResponseErrorHandler:
    def __init__(self, app: Flask):
        @app.errorhandler(APIResponseError)
        def handle_invalid_usage(error):
            app.logger.error(error.to_dict())
            response = jsonify(error.to_dict())
            response.status_code = error.status_code
            return response

        @app.errorhandler(404)
        def resource_not_found(e):
            response = jsonify({'status': 'error', 'message': str(e)})
            response.status_code = 404
            return response

        @app.errorhandler(Exception)
        def handle_exception(error):
            app.logger.error(str(error))
            response = jsonify({
                'status': 'error',
                'message': 'Internal Server Error'
            })
            response.status_code = 500
            return response
