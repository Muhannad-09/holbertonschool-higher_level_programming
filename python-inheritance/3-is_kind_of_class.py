#!/usr/bin/python3
"""
Module for checking if an object is instance or subclass instance.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class
    or inherits from it, else False.
    """
    return isinstance(obj, a_class)
