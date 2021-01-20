#!/usr/bin/python3
"""Contains text file manipulation function(s)"""


def append_write(filename="", text=""):
    """Writes to a file in utf8 encoding"""
    if filename:
        with open(filename, mode='a', encoding='utf8') as f:
            return f.write(text)
