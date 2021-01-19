#!/usr/bin/python3
"""A module about geometric shapes"""


class BaseGeometry:
    """Base claas for geometric shapes"""
    def area(self):
        """Calculates the area of a given geometric shape"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates that value is an integer, triggers an exception
            otherwise
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
