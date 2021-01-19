#!/usr/binpython3
"""Instance helper function(s)"""

def inherits_from(obj, a_class):
    """Checks if an object is an instance of a subclass of the given class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
