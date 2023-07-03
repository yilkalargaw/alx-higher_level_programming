#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """ Rectangle Class"""

    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

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

        return ((lambda h, w: "\n"
                 .join([(str(self.print_symbol) * w) for i in range(h)]))
                (self.height, self.width))

    def __repr__(self):
        """ Returns the representation of Rectangle class.
        Arg:
           NONE
        Return:
            representaion of the rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """ Deletes last instance
        Arg:
           NONE
        Return:
            NONE
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares Rectangles
        Arg:
            rect_1: (rect)
            rect_2: (rect)
        Return:
            the bigger one of the rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
