#!/usr/bin/python3
"""Input Output Practice"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”:
    Arg:
        my_obj:
    Return:
        JSON of string
    """
    with open(filename, 'r') as f:
        return (json.load(f))
