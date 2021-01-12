#!/usr/bin/python3
"""Contains a locked Class"""


class LockedClass:
    """A class that prevents the user from dynamically creating new instance
        attributes, except if the new instance attribute is called first_name
    """
    def __setattr__(self, name, value):
        """Overides the default behaviour os setting an attribute on a
            LockedClass object
        """
        if name != 'first_name':
            raise AttributeError("'{}' object has no \
attribute '{}'".format(self.__class__.__name__, name))
        self.__dict__[name] = value
