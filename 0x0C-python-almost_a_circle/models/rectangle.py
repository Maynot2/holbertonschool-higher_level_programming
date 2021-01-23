#!/usr/bin/python3

"""
    Contains a Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """
        Simulates a real life Rectangle
        private instance attributes:
            __width
            __height
            __x
            __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes Rectangle object with given:
            width, height, x, y and id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Getter for widh attribute"""
            return self.__width

        @width.setter
        def width(self, val):
            """Setter for widh attribute"""
            self.__width == val

        @property
        def height(self):
            """Getter for height attribute"""
            return self.__height

        @height.setter
        def height(self, val):
            """Setter for height attribute"""
            self.__height == val

        @property
        def x(self):
            """Getter for height attribute"""
            return self.__x

        @x.setter
        def x(self, val):
            """Setter for height attribute"""
            self.__x == val

        @property
        def y(self):
            """Getter for height attribute"""
            return self.__y

        @y.setter
        def y(self, val):
            """Setter for height attribute"""
            self.__y == val
