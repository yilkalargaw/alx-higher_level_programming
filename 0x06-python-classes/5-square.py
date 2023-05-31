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

    @property
    def size(self):
        """Retrieves size
        Return:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size
        Arg:
            value: set by user for square size
        Return:
            None
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        else:
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """Calculates area of a square
        Return:
            Area (int)
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Prints square using area
        Return:
            None
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print('*' * self.size)
