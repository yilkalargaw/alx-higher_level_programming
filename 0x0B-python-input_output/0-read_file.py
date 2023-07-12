#!/usr/bin/python3
"""IO Practice"""


def read_file(filename=""):
    """read UTF-8 encoded text from file
    Arg:
        filename:

    Return:

    """
    with open(filename, 'r', encoding='UTF8') as reading:
        print(reading.read(), end="")
