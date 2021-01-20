#!/usr/bin/python3
"""Holds a student class"""


class Student:
    """Models a real life student"""
    def __init__(self, first_name, last_name, age):
        """
            Initializes a student instance with a given first_name, last_name
            and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return vars(self)
