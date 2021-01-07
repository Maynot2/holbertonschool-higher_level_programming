#!/usr/bin/python3
"""Contains a simple add function"""


def add_integer(a, b=98):
    """Adds 2 integers"""

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    print(add_integer(1, 2, 3))

