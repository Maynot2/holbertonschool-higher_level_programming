#!/usr/bin/python3


"""This is the documentation for 0-square module"""


class Square:
    """
        Models a real life square with a size attribute
        and an area method to compute the size of a
        given square
    """

    def __init__(self, size=0):
        """Constructor method for square instances"""

        self.size = size

    @property
    def size(self):
        """Getter method for size property"""

        return self.__size

    @size.setter
    def size(self, val):
        """Setter method for size property"""

        if not isinstance(val, int):
            raise TypeError('size must be an integer')
        if val < 0:
            raise ValueError('size must be >= 0')
        self.__size = val

    def area(self):
        """Computes the area of a square given the size of one of its sides"""

        return self.size ** 2

    def __lt__(self, sqr):
        return self.size < sqr.size

    def __le__(self, sqr):
        return self.size <= sqr.size

    def __gt__(self, sqr):
        return self.size > sqr.size

    def __ge__(self, sqr):
        return self.size >= sqr.size

    def __eq__(self, sqr):
        return self.size == sqr.size

    def __ne__(self, sqr):
        return self.size != sqr.size
