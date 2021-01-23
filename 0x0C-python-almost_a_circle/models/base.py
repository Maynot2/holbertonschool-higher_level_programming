#!/usr/bin/python3

"""
    Contains the Base class for geometric shapes
"""


class Base:
    """
        The base class for geometric shapes
        class attributes:
            __nb_objects
        instance attributes:
            id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes base object with given id"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
