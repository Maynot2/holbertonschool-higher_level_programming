#!/usr/bin/python3
"""Contains jason file and jason string manipulation function(s)"""
import json


def load_from_json_file(filename):
    """Load json file and truns it into python object"""
    if filename:
        with open(filename) as f:
            return json.load(f)

