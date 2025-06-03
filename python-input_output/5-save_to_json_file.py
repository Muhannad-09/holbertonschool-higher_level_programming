#!/usr/bin/python3
"""
This module provides a function to save a Python object
to a file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj: The object to serialize to JSON.
        filename (str): The file path to write the JSON string.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
