import re

ALLOWED_TYPES = (str, bool, int, float, dict, list)


class AbstractRule(object):

    def validate(self, value):
        """
        :param mixed value:
        :rtype: list|None
        :return: errors
        :rtype: list
        """
        raise NotImplementedError()


class CompositeRule(object):

    def __init__(self, *rules):
        self.rules = rules

    def __iter__(self):
        for rule in self.rules:
            yield rule


class Pattern(AbstractRule):

    def __init__(self, pattern):
        """
        :param str pattern:
        """
        self.pattern = re.compile(pattern)

    def validate(self, value):
        errors = []
        if not self.pattern.search(value):
            errors.append('Value "{}" does not match pattern "{}"'.format(value, self.pattern.pattern))
        return errors


class Enum(AbstractRule):

    def __init__(self, *allowed_values):
        self.allowed_values = allowed_values

    def validate(self, value):
        errors = []
        if value not in self.allowed_values:
            errors.append('Incorrect value "{}". Allowed values: {}'.format(value, self.allowed_values))
        return errors


class MaxLength(AbstractRule):

    def __init__(self, length):
        """

        :param int length:
        """
        self.length = length

    def validate(self, value):
        errors = []
        if len(value) > self.length:
            errors.append('Invalid length for value "{}". Max length = {}'.format(value, self.length))
        return errors


class MinLength(AbstractRule):

    def __init__(self, length):
        """

        :param int length:
        """
        self.length = length

    def validate(self, value):
        errors = []
        if len(value) < self.length:
            errors.append('Invalid length for value "{}". Min length = {}'.format(value, self.length))
        return errors

class Email(AbstractRule):

    def __init__(self):
        """
        :param str pattern:
        """
        self.pattern = re.compile(r'^[a-z][a-z0-9_\.]{0,32}@[a-z0-9]{2,}(\.[a-z0-9]{2,4}){1,2}$')

    def validate(self, value):
        errors = []
        if not self.pattern.search(value):
            errors.append('{} is not a email'.format(value))
        return errors