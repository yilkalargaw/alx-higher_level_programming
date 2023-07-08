#!/usr/bin/python3
"""
TDD Practice
"""


def text_indentation(text):
    """ print new lines and indent
    Arg:
        text:
    Return:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    indented = text

    for x in ".?:":
        t = indented.split(x)
        indented = ""
        for y in t:
            y = y.strip(" ")

            if indented == "":
                indented = y + x
            else:
                indented = indented + "\n\n" + y + x

    print(indented[:-3], end="")
