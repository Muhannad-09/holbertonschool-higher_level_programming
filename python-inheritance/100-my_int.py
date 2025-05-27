#!/usr/bin/python3
"""
Defines class MyInt that inverts == and != operators.
"""


class MyInt(int):
    """A rebel int class that inverts equality operators."""

    def __eq__(self, other):
        """Invert equality: return False if equal."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert inequality: return True if equal."""
        return super().__eq__(other)
