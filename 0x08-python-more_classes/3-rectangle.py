#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """ Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Rectangle class Constructor.
        Arg:
            width: (int)
            height: (int)

        Return:
            None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width Getter.
        Arg:
           NONE

        Return:
            width
        """
        return self.__width

    @property
    def height(self):
        """Height. Getter
        Arg:
           NONE

        Return:
            height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Width Setter.
        Arg:
            value: (int)

        Return:
            NONE
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Height Setter.
        Arg:
            value: (int)

        Return:
            NONE
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Area Calculator.
        Arg:
           NONE

        Return:
            area: (int)
        """
        return (self.width * self.height)

    def perimeter(self):
        """Perimeter Calculator.
        Arg:
           NONE

        Return:
            perimeter: (int)
        """
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """ Returns the str representation of Rectangle class.
        Arg:
           NONE
        Return:
            str of the rectangle
        """

        if self.height == 0 or self.width == 0:
            return ""

        return ((lambda h, w: "\n".join(["#"*w for i in range(h)]))
                (self.height, self.width))
