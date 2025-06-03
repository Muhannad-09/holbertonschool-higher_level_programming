#!/usr/bin/python3
"""
This module defines a Student class that supports
serialization to JSON and reloading from JSON.
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
        Retrieves a dictionary representation of the Student instance.
        If attrs is a list of strings, only attributes named in this list
        will be included. Otherwise, all attributes are included.

        Args:
            attrs (list or None): List of attribute names to include.

        Returns:
            dict: Dictionary representation of the Student.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those
        in the provided dictionary.

        Args:
            json (dict): Dictionary of attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
