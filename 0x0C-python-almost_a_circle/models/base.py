#!/usr/bin/python3

"""
    Contains the Base class for geometric shapes
"""

import json


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
        if not list_dictionaries:
            return '[]'
        else:
            return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        filename = '{}.json'.format(cls.__name__)
        with open(filename, mode='w') as f:
            f.write(cls.to_json_string(list_dicts))
