#!/usr/bin/env python3
"""Pickle a custom object."""

import pickle


class CustomObject:
    """Custom object with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initialize attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle.

        Args:
            filename (str): The file name to save the object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject from a file.

        Args:
            filename (str): The file name to load the object from.

        Returns:
            CustomObject or None if error.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None
