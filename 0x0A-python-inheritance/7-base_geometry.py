#!/usr/bin/python3
"""an empty class BaseGeometry."""


class BaseGeometry:
    """represents a base geometry"""

    def area(self):
        """returns area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates if a parameter as an integer.
        Args:
            name(str): the name of the parameter.
            value(int): the parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
