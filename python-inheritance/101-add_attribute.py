#!/usr/bin/python3
"""
Function to add a new attribute to an object if possible.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's allowed.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
