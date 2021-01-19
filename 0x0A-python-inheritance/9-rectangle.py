#!/usr/binpython3
"""A module about geometric shapes"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes a rectangle with a given width and length"""
        self.integer_validator(width)
        self.integer_validator(height)
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method for width attribute"""
        self.__width = width

    @property
    def height(self):
        """Getter method for height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for height  attribute"""
        self.__height = height

    def __str__(self):
        """Overides internal string representation of rectangle object"""
        return '[{}] {}/{}'.format(type(self).__name__,
                                   self.width, self.height)

    def area(self):
        """Computes the area of a rectangle of a given width and length"""
        return self.width * self.height
