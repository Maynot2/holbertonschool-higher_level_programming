#!/usr/binpython3
"""A module about geometric shapes"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes a rectangle with a given width and length"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Overides internal string representation of rectangle object"""
        return '[{}] {}/{}'.format(type(self).__name__,
                                   self.__width, self.__height)

    def area(self):
        """Computes the area of a rectangle of a given width and length"""
        return self.__width * self.__height
