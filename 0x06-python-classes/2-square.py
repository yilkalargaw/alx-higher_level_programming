#!/usr/bin/python3
"""Square people accepted here"""


class Square:
    """A class to define squareness

    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        """Initializes a square
        Arg:
            size (int): size of square
        """

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif (type(size) is int) and size < 0:
            raise ValueError("Size must be greater than or equal to 0")
        else:
            self.__size = size
