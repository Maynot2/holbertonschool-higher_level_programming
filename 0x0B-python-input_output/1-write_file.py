#!/usr/bin/python3
"""Contains text file manipulation function(s)"""


def write_file(filename="", text=""):
    """Writes to a file in utf8 encoding"""
    if filename:
        with open(filename, mode='w', encoding='utf8') as f:
            return f.write(text)
