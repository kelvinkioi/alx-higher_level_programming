#!/usr/bin/python3
"""defines a function that checks for an object in a class"""


def is_same_class(obj, a_class):
    """Checks if obj is exactly an instance of a_class
    Args:
        obj: the object
        a_class: the class to compare with the object
    Returns:
        True if the object is exactly an instance of the
        specified class; otherwise False
    """

    if type(obj) == a_class:
        return True
    return False
