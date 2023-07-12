#!/usr/bin/python3
"""Input Output Practice"""


def append_write(filename="", text=""):
    """append a string at the end of a text file (UTF8) and
       return the number of characters added
    Arg:
        filename:

    Return:

    """

    with open(filename, 'a', encoding='UTF8') as f:
        appended = f.write(text)
        return appended
