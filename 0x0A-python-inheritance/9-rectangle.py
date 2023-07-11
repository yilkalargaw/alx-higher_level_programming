#!/usr/bin/python3
"""Inheritance Practice"""

basegeo = __import__('7-base_geometry').BaseGeometry


class Rectangle(basegeo):
    """BaseGeometry >> Rectangle"""

    def __init__(self, width, height):
        """constructor
        Arg:
            width:
            height:
        Return:
            NONE
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """calculate area
        Return:
            area
        """
        return (self.__height * self.__width)

    def __str__(self):
        """string form
        Return:
            str of rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
