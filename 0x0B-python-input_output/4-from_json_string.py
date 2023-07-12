#!/usr/bin/python3
"""Input Output Practice"""

import json


def from_json_string(my_str):
    """returns an object (Python data structure)
       represented by a JSON string:
    Arg:
        my_obj:
    Return:
        JSON of string
    """
    return (json.loads(my_str))
