#!/usr/bin/python3


"""This is the documentation for 0-square module"""


class Square:
    """Models a real life square with a size attribute"""

    def __init__(self, size=0):
        """Constructor method for square instances"""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Computes the area of a square given the size of one of its sides"""

        return self.__size ** 2
