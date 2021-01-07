#!/usr/bin/python3
"""Contains a simple add function"""
import math


def add_integer(a, b=98):
    """Adds 2 integers"""

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if float('-inf') == a or float('inf') == a:
        raise TypeError('a must be an integer')
    if float('-inf') == b or float('inf') == b:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
