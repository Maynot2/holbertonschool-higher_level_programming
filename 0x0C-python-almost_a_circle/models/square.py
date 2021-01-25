#!/usr/bin/python3

"""
    Contains a Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Simulates a real life Square
        inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes Rectangle object with given:
            width, height, x, y and id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Retrun a custom representation of a rectangle object for print()"""
        return '[{}] ({}) {}/{} - {}/{}'.format(type(self).__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height)
