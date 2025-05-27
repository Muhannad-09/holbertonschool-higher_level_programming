#!/usr/bin/python3
"""
This module defines a class that inherits from list
and provides a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print
    the list in ascending sorted order without modifying the original.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
