#!/usr/bin/python3
"""Inheritance Practice"""


def inherits_from(obj, a_class):
    """ checks if an object is instance of the specified class
    Arg:
        obj:
        a_class:
    Return:
        True or False
    """

    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
