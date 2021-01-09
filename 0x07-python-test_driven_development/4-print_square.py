#!/usr/bin/python3
"""Contains function(s) to print geometric shapes"""


def print_square(size):
    """Prints a square of '#' symbols given a size"""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)
