#!/usr/bin/python3
"""
This module provides a function to convert a JSON string
into a corresponding Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object representation of a JSON string.

    Args:
        my_str (str): JSON-formatted string.

    Returns:
        object: Python object resulting from decoding JSON.
    """
    return json.loads(my_str)
