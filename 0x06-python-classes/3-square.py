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

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (type(size) is int) and size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates area of a square"
        """
        return (self.__size ** 2)
