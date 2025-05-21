#!/usr/bin/python3
"""Defines a Rectangle class with instance counting."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0  # public class attribute

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        If width or height is 0, return 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.
        If width or height is 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        lines = ["#" * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """
        Return a string that can recreate the rectangle using eval().
        Example: Rectangle(2, 4)
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message and update instance count when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
