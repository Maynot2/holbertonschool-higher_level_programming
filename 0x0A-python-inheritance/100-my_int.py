#!/usr/bin/python3
"""A module that tweak the int class"""


class MyInt(int):
    """Overloads some of the default int methods"""
    def __init__(self, i):
        """Initializes a MyInt object"""
        if type(i) == int:
            self._value = i

    def __eq__(self, other):
        """Overides == method"""
        return self._value != other

    def __ne__(self, other):
        """Overides != method"""
        return self._value == other
