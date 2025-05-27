#!/usr/bin/python3
"""
Defines class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """BaseGeometry class with an unimplemented area method."""

    def area(self):
        """Raises an Exception when called, because it's not implemented."""
        raise Exception("area() is not implemented")
