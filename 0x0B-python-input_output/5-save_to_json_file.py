#!/usr/bin/python3
"""Contains jason file and jason string manipulation function(s)"""
import json


def save_to_json_file(my_obj, filename):
    """A python object as a jason file"""
    if my_obj and filename:
        with open(filename, mode='w') as f:
            json.dump(my_obj, f)

