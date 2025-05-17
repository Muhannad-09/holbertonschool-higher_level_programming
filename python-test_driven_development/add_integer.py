#!/usr/bin/python3

"""
This module provides a function that adds two numbers.

The function ensures that the inputs are integers or floats.
It will cast float arguments to integers before performing addition.
If the inputs are not numbers, it raises a TypeError.
The goal is to safely perform integer addition with type checking.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats after casting them to integers.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
