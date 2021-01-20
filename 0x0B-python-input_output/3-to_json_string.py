#!/usr/bin/python3
"""Contains jason file and jason string manipulation function(s)"""
import json


def to_json_string(my_obj):
    """Turns a python object into a jason string"""
    return json.dumps(my_obj)
