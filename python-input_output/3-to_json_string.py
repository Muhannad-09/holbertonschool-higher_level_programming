#!/usr/bin/python3
"""
This module provides a function to convert a Python object to
its JSON string representation.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object (string).

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
