#!/usr/bin/python3
"""
This module provides a function to return the dictionary
representation of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: Dictionary containing all serializable attributes.
    """
    return obj.__dict__
