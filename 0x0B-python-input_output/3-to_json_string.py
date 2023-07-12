#!/usr/bin/python3
"""Input Output Practice"""

import json


def to_json_string(my_obj):
    """ return the JSON representation of an object (string):
    Arg:
        my_obj:
    Return:
        JSON of string
    """
    return (json.dumps(my_obj))
