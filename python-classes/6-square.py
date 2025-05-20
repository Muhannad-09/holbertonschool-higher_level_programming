#!/usr/bin/python3
"""This module defines a Square class with position and printing features."""


class Square:
    """Represents a square with size, position, and printable output."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The (x, y) coordinates for positioning the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): A tuple representing (x, y) coordinates.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters, adjusting for position."""
        if self.__size == 0:
            print()
            return

        # Print vertical spaces (y-axis offset)
        for _ in range(self.__position[1]):
            print()

        # Print the square with horizontal spaces (x-axis offset)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
