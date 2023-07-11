#!/usr/bin/python3
"""Inheritance Practice"""


def is_kind_of_class(obj, a_class):
    """ checks if the object is aninstance of the some class
    Arg:
        obj:
        a_class:
    Return:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
