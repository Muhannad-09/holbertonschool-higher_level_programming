#!/usr/bin/python3
"""
This module defines a Student class with a method to retrieve
its dictionary representation for JSON serialization.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: Dictionary containing student's attributes.
        """
        return self.__dict__
