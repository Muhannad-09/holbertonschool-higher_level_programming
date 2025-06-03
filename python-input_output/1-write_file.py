#!/usr/bin/python3
"""
This module provides a function to write text to a UTF-8 text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write.

    Returns:
        int: Number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
