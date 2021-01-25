#!/usr/bin/python3

"""
    Contains a Rectangle class
"""

from models.base import Base


def integer_validator(name, val):
    """Raises Error if val is not an integer"""
    if type(val) != int:
        raise TypeError('{} must be an integer'.format(name))


def positive_integer_validator(name, val):
    """Raises an Error if val is not an integer or inferior to 0"""
    integer_validator(name, val)
    if val < 0:
        raise ValueError('{} must be >= 0'.format(name))


def strict_positive_integer_validator(name, val):
    """Raises an Error if val is not an integer or inferior to 1"""
    integer_validator(name, val)
    if val < 1:
        raise ValueError('{} must be > 0'.format(name))


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
        strict_positive_integer_validator('width', val)
        self.__width = val

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, val):
        """Setter for height attribute"""
        strict_positive_integer_validator('height', val)
        self.__height = val

    @property
    def x(self):
        """Getter for height attribute"""
        return self.__x

    @x.setter
    def x(self, val):
        """Setter for height attribute"""
        positive_integer_validator('x', val)
        self.__x = val

    @property
    def y(self):
        """Getter for height attribute"""
        return self.__y

    @y.setter
    def y(self, val):
        """Setter for height attribute"""
        positive_integer_validator('y', val)
        self.__y = val

    def area(self):
        """Conputes the area of a rectangle given a height and width"""
        return self.width * self.height

    def display(self):
        for i in range(self.height + self.y):
            if i < self.y:
                print()
            else:
                print((' ' * self.x) + ('#' * self.width))

    def __str__(self):
        """Retrun a custom representation of a rectangle object for print()"""
        return '[{}] ({}) {}/{} - {}/{}'.format(type(self).__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height)

    def update(self, *args, **kargs):
        """Update attributes in this order id, width, height, x, y"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        size = len(args) if len(args) <= len(attrs) else len(attrs)
        i = 0
        for attr in attrs[:size]:
            setattr(self, attr, args[i])
            i += 1
        if not args and kargs:
            for k, v in kargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
