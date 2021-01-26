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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def __str__(self):
        """Retrun a custom representation of a square object for print()"""
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.size)

    def update(self, *args, **kargs):
        """Update attributes in this order id, size, x, y"""
        attrs = ['id', 'size', 'x', 'y']
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
        """Transform a square into a dictionary"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'size': self.size,
        }
