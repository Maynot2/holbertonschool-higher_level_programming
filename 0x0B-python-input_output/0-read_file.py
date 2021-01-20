#!/usr/bin/python3
"""Contains text file manipulation function(s)"""


def read_file(filename=""):
    """Reads a file with utf8 encoding"""
    if filename:
        with open(filename, encoding='utf8') as f:
            print(f.read(), end='')
