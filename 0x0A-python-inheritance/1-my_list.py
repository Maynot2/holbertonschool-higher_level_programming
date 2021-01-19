#!/usr/bin/python3
"""Custom list behavior"""


class MyList(list):
    """Manipulates lists"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
