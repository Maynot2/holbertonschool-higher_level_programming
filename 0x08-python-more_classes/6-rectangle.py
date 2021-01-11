#!/usr/bin/python3
"""This module contains geometric shape classe(s)"""


class Rectangle:
    """Simulates a real world rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialises a rectangle of a given width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, size):
        """Sets the width"""
        if not isinstance(size, int):
            raise TypeError('width must be an integer')
        if size < 0:
            raise ValueError('width must be >= 0')
        self.__width = size

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, size):
        """Sets the height"""
        if not isinstance(size, int):
            raise TypeError('height must be an integer')
        if size < 0:
            raise ValueError('height must be >= 0')
        self.__height = size

    def area(self):
        """Computes the area"""
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """Returns a string representation of the rectangle"""
        str_ = ''
        if self.width == 0 or self.height == 0:
            return str_
        for i in range(self.height):
            str_ += '#' * self.width
            if i < self.height - 1:
                str_ += '\n'
        return str_

    def __repr__(self):
        """Returns a string representation of the current instance that can be
            evaluated by eval
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """Deletes the current rectangle"""
        print('Bye rectangle...')
        type(self).number_of_instances -= 1
