#!/usr/bin/python3
"""Instance helper function(s)"""


def is_same_class(obj, a_class):
    """Checks if an object is stricly of given class (not a subclass)"""
    return type(obj) == a_class
