#!/usr/bin/python3

"""
    Contains the Base class for geometric shapes
"""

import json
import os.path
import csv


def is_list_of_dicts(l):
    """Check if passed argument l is a list of dicts"""
    if type(l) is not list:
        return False
    for item in l:
        if type(item) is not dict:
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
        if type(l) is not list:
            return False
        for item in l:
            if not isinstance(item, cls):
                return False
        return True

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of shapes to a JSON file"""
        if cls.is_list_of_shapes(list_objs):
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            filename = '{}.json'.format(cls.__name__)
            with open(filename, mode='w') as f:
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create new instance from dictionary"""
        shape = cls(1, 1)
        shape.update(**dictionary)
        return shape

    @classmethod
    def load_from_file(cls):
        """Create a list of instances from JSON file"""
        list_shapes = []
        filename = '{}.json'.format(cls.__name__)
        if os.path.isfile(filename):
            with open(filename) as f:
                shapes = cls.from_json_string(f.read())
                for shape in shapes:
                    list_shapes.append(cls.create(**shape))
        return list_shapes

    @staticmethod
    def is_given_obj_list(objtype, list_objs):
        for obj in list_objs:
            if obj.__class__.__name__ != objtype:
                return False
        return True

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of shapes to a CSV file"""
        filename = '{}.csv'.format(cls.__name__)
        with open(filename, mode='w') as cvs_file:
            cvs_writer = csv.writer(cvs_file)
            if cls.is_given_obj_list('Rectangle', list_objs):
                fields = ['id', 'width', 'height', 'x', 'y']
                cvs_writer.writerow(fields)
                for shape in list_objs:
                    cvs_writer.writerow([shape.id,
                                         shape.width,
                                         shape.height,
                                         shape.x,
                                         shape.y])
            if cls.is_given_obj_list('Square', list_objs):
                fields = ['id', 'size', 'x', 'y']
                cvs_writer.writerow(fields)
                for shape in list_objs:
                    cvs_writer.writerow([shape.id,
                                         shape.size,
                                         shape.x,
                                         shape.y])

    @classmethod
    def load_from_file_csv(cls):
        """Create a list of instances from CSV file"""
        list_shapes = []
        filename = '{}.csv'.format(cls.__name__)
        if os.path.isfile(filename):
            with open(filename) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    for keys in row:
                        row[keys] = int(row[keys])
                    list_shapes.append(cls.create(**row))
        return list_shapes
