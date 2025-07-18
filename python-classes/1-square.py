#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """Represents a square."""
    def __init__(self, size):
        """"Initialize the square with a given size.

Args:
            size: The size of the square.
        """
        self.__size = size
