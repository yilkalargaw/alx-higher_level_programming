#!/usr/bin/python3
"""IO Practice"""


"""
Student Class.

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
        Initializes parameters of a new Student object.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of the student.

        Args:
            attrs:

        Returns:
            dict: A dict containing first name, last name, and age.
        """

        def to_json(self, attribute_list=None):
            if attribute_list is not None:
                return {attribute: self.__dict__[attribute]
                        for attribute in self.__dict__.keys() & attribute_list}
            else:
                return self.__dict__

# def default(self, o):
#         return o.__dict__
