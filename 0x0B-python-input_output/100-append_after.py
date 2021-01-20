#!/usr/bin/python3
"""Append a line after a certain string is encountered"""


def append_after(filename="", search_string="", new_string=""):
    """Append after line"""
    with open(filename, encoding='utf8') as f:
        text = f.readlines()
    with open(filename, mode='w', encoding='utf8') as f:
        for line in text:
            if search_string in line:
                line += new_string
            f.write(line)
