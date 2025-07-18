#!/usr/bin/python3
"""
This module defines a Student class with support for
filtered dictionary conversion for JSON serialization.
"""


class Student:
    """
    Defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

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
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes in this list
        are included.

        Args:
            attrs (list or None): Optional list of attribute names to include.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
