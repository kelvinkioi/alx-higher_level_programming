#!/usr/bin/python3
"""Defines a function taht checks the object is an instance of
or if the object is an instance of a class that inherited from
the specified class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is the same class or inherit from the class
    Args:
        obj: the object
        a_class: the class
    Returns:
        True if the object is an instance or inherit from the
        specified class, otherwise False
    """

    if isinstance(obj, a_class):
        return True
    return False
