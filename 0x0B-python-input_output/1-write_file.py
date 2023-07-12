#!/usr/bin/python3
"""IO Practice"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
       return the number of characters written
    Arg:
        filename:

    Return:

    """

    with open(filename, 'w', encoding='UTF8') as f:
        f.write(text)

    charcount = 0

    with open(filename, 'r') as f:
        charcount = len(f.read())

    return (charcount)
