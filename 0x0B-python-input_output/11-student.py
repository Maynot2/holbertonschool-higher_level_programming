#!/usr/bin/python3
"""Holds a student class"""


def is_str_list(ary):
    """Checks if all elements of a list are strings"""
    if type(ary) != list:
        return False
    for elm in ary:
        if type(elm) != str:
            return False
    return True


class Student:
    """Models a real life student"""
    def __init__(self, first_name, last_name, age):
        """
            Initializes a student instance with a given first_name, last_name
            and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if is_str_list(attrs):
            return {k: v for k, v in vars(self).items() if k in attrs}
        else:
            return vars(self)

    def reload_from_json(self, json):
        keys = list(self.to_json(self).keys())
        for k in keys:
            delattr(self, k)
        for k, v in json.items():
            setattr(self, k, v)
