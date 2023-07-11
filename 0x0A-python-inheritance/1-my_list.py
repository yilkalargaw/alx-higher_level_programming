#!/usr/bin/python3
"""Inheritance Practice"""


class MyList(list):
    """A class"""


    def print_sorted(self):
        """Returns a list with the available
        attributes and methods in an object
        Arg:

        Return:
          NULL
        """
        print(sorted(self))
