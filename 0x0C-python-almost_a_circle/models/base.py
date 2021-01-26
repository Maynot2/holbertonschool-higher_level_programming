#!/usr/bin/python3

"""
    Contains the Base class for geometric shapes
"""

import json


def is_list_of_dicts(self):
    """Check if passed argument l is a list of dicts"""
    if type(l) not list:
        return False
    for item in l:
        if type(item) not dict:
            return False
    return True


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to json strings"""
        if list_dictionaries == [] or list_dictionaries is None:
            return '[]'
        if is_list_of_dicts(list_dictionaries):
            return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def is_list_of_shapes(cls, l):
        """Check if passed argument l is a list of shapes"""
        if type(l) not list:
            return False
        for item in l:
            if not isinstance(item, cls):
                return False
        return True

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of shapes to a file"""
        if cls.is_list_of_shapes(list_objs):
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            filename = '{}.json'.format(cls.__name__)
            with open(filename, mode='w') as f:
                f.write(cls.to_json_string(list_dicts))
