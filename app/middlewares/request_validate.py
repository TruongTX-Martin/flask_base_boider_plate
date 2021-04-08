import types
from flask import request
from functools import wraps
from .validators.exceptions import *
from .validators.params import *
from .validators.rules import *

def request_validate(*params):
    """
    Validate route of request. Example:

    @app.route('/example')
    @request_validate(
        # FORM param(request.form)
        Param('param_name', FROM, ...),
        # PATH param(part of route - request.view_args)
        Param('level', PATH, rules=[Pattern(r'^[a-zA-Z0-9-_.]{5,20}$')]),
    )
    def example_route(level):
        ...
    """
    print('start validate data');
    def validate_params(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            errors, endpoint_args = __get_errors(params)
            if errors:
                raise InvalidRequest(errors)

            if args:
                endpoint_args = (args[0], ) + tuple(endpoint_args)

            return func(*args, **kwargs)

        return wrapper

    return validate_params


def __get_errors(params):
    """
    Returns errors of validation and valid values
    :param tuple params: (Param(), Param(), ...)
    :rtype: list
    :return:
        {{'param_name': ['error1', 'error2', ...], ...},
        [value1, value2, value3, ...]
    """

    errors = {}
    valid_values = []

    for param in params:
        param_name = param.name
        param_type = param.param_type
        value = __get_request_value(param_type, param_name)

        if value is None:
            if param.required:
                errors[param_name] = ['Value is required']

                continue
            else:
                if param.default is not None:
                    if isinstance(param.default, types.LambdaType):
                        value = param.default()
                    else:
                        value = param.default

                valid_values.append(value)

                continue
        else:
            if param.value_type:
                try:
                    value = param.value_to_type(value)
                except (ValueError, TypeError):
                    errors[param_name] = [
                        'Error of conversion value "%s" to type %s' %
                        (value, param.value_type)
                    ]

                    continue

                if param.value_type != type(value):
                    errors[param_name] = [
                        'Error of conversion value "%s" to type %s' %
                        (value, param.value_type)
                    ]

                    continue

            rules_errors = []
            for rule in param.rules:
                rules_errors.extend(rule.validate(value))

            if rules_errors:
                errors[param_name] = rules_errors
            else:
                valid_values.append(value)

    return errors, valid_values


def __get_request_value(value_type, name):
    """
    :param str value_type: POST, GET or VIEW
    :param str name:
    :raise: UndefinedParamType
    :return: mixed
    """
    if value_type == 'FORM':
        return request.form.get(name)
    elif value_type == 'GET':
        value = request.args.getlist(name)
        return ",".join(value) if value else None
    elif value_type == 'PATH':
        return request.view_args.get(name)
    elif value_type == 'JSON':
        json_ = request.get_json()
        return json_.get(name) if json_ else json_
    else:
        raise UndefinedParamType('Undefined param type %s' % name)