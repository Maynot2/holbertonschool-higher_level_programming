#!/usr/bin/python3
"""Contains function(s) to print geometric shapes"""


def print_square(size):
    """Prints a square of '#' symbols given a size"""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    # if size == 0:
        # print()
    for i in range(size):
        print('#' * size)

if __name__ == "__main__":
    print_square(0)
