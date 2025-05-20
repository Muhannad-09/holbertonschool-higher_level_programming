#!/usr/bin/python3
"""This module defines a Square class that can print itself."""


class Square:
    """Represents a square with size, area, and printable output."""

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
