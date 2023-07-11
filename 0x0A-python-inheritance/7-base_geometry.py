#!/usr/bin/python3
"""Inheritance Practice"""


class BaseGeometry():
    """basegeometry class
    Return:
    """
    def area(self):
        e = "area() is not implemented"
        raise Exception(e)

    def integer_validator(self, name, value):
        """validate a value
        Arg:
            name:
            value:
        Return:
            NONE
        """
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        self.value = value
