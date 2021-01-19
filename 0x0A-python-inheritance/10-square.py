#!/usr/bin/python3
"""A module about geometric shapes"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class inheriting from Rectangle"""
    def __init__(self, size):
        """Initializes a square with a given side size"""
        self.integer_validator('side', size)
        super().__init__(size, size)
        self.__size = size
