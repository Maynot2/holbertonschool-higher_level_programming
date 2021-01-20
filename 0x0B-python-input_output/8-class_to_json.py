#!/usr/bin/python3
"""Format object to trun into json"""


def class_to_json(obj):
    """Create a python dict with the attribute key/value pairs of an object """
    return vars(obj)
