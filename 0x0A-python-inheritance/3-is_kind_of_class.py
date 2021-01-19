#!/usr/bin/python3
"""Instance helper function(s)"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is of given class or subclass of the given class)"""
    return isinstance(obj, a_class)
