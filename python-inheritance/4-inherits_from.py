#!/usr/bin/python3
"""
Defines a function inherits_from that returns True
if the object is an instance of a class that
inherits (directly or indirectly) from the specified class,
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class,
    but not if obj is exactly an instance of a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
