#!/usr/bin/python3
"""IO Practice"""


def class_to_json(obj):
    """returns the dictionary description with simple
       data structure (list, dictionary, string, integer
       and boolean) for JSON serialization of an object:
    Arg:
        obj: object
    Return:
        dict_rep_of obj
    """
    return obj.__dict__
