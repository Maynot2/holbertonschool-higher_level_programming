#!/usr/bin/python3
"""A module about geometric shapes"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """Imitializes a rectangle with a given width and length"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
