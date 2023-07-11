#!/usr/bin/python3
"""Inheritance Practice"""


def is_same_class(obj, a_class):
    """ checks if the object is an instance of some class
    Arg:
        obj:
        a_class:
    Return:
        True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
