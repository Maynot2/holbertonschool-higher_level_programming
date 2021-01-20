#!/usr/bin/python3
"""Contains jason file and jason string manipulation function(s)"""
import json


def from_json_string(my_str):
    """Turns a jason string into a python object"""
    if my_str:
        return json.loads(my_str)
