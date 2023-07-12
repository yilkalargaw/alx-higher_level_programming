#!/usr/bin/python3
"""IO Practice"""


"""
This class represents a student.

Attributes:
    first_name (str):
    last_name (str):
    age (int):

Methods:
    to_json():
"""


class Student:

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student object.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the student.

        Returns:
            dict: A dict containing first name, last name, and age.
        """

        return (self.__dict__)
