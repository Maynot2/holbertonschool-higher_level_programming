#!/usr/binpython3
"""A module about geometric shapes"""

class BaseGeometry:
    """Base claas for geometric shapes"""
    def area(self):
        """Calculates the area of a given geometric shape"""
        raise Exception('area() is not implemented')
