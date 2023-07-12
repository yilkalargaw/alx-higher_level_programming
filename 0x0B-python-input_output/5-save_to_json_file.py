#!/usr/bin/python3
"""Input Output Practice"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation:
    Arg:
        my_obj:
    Return:
        JSON of string
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
