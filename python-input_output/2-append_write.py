#!/usr/bin/python3
"""
This module provides a function to append text to a UTF-8 text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The string to append.

    Returns:
        int: Number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
