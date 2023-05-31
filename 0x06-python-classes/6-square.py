#!/usr/bin/python3
"""Square people accepted here"""


class Square:
    """A class to define squareness

    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Arg:
            size (int): size of square
        """

        self.position = position
        self.size = size

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

    @property
    def position(self):
        """Gets position cooridinate
        Return:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position
        arg:
            value: set to position the square from start
        Return:
            None
        """
        if type(value) != tuple or len(value) != 2 or \
           type(value[0]) != int or type(value[1]) != int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        print("\n" * self.position[1], end='')
        for i in range(self.size):
            print((' ' * self.position[0]) + ('#' * self.size))
