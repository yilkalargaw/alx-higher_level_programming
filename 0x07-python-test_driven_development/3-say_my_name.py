#!/usr/bin/python3
"""
TDD Practice
"""


def say_my_name(first_name, last_name=""):
    """return first and last names
    Arg:
        first_name:
        last_name:
    Return:
        Full Name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
