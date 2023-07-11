#!/usr/bin/python3
"""Inheritance Practice"""

rect = __import__('9-rectangle').Rectangle


class Square(rect):
    """BaseGeometry >> Rectangle"""

    def __init__(self, size):
        """constructor
        Arg:
            size
        Return:
            NONE
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """calculate area
        Return:
            area
        """
        return (self.__size ** 2)

    def __str__(self):
        """string form
        Return:
            str of rectangle
        """
        return f"[Square] {self.__size}/{self.__size}"
