#!/usr/bin/python3


"""This is the documentation for 0-square module"""


class Square:
    """
        Models a real life square with a size attribute
        and an area method to compute the size of a
        given square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Constructor method for square instances"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method for position property"""

        return self.__position

    @position.setter
    def position(self, val):
        """Setter method for position property"""

        if not isinstance(val, tuple) or len(val) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if val[0] < 0 or val[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = val

    def area(self):
        """Computes the area of a square given the size of one of its sides"""

        return self.size ** 2

    def my_print(self):
        """Prints a square of a given size"""

        if self.size == 0:
            print()
        for i in range(self.size + self.position[1]):
            if i >= self.position[1]:
                for j in range(self.size + self.position[0]):
                    if j < self.position[0]:
                        print('_', end='')
                    else:
                        print('#', end='')
            print()
