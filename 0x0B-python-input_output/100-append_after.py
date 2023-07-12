#!/usr/bin/python3
"""IO Practice"""


def append_after(filename="", search_string="", new_string=""):
    """append after function
    Arg:
        filename:
        search_string:
        new_string:
    Return:
        NONE
    """

    with open(filename, "r") as f:
        lines = f.readlines()

    lines = list(map(lambda line:
                     line if search_string not in line
                     else line + new_string, lines))

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
