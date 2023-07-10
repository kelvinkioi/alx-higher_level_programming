#!/usr/bin/python3
"""an inherited class_checking function."""


def inherits_from(obj, a_class):
    """
    function returns True if the
    object is an instance of a class that inherited
    (directly or indirectly) from the specified class,
    otherwise False.
    Args:
        obj: the object
        a_class: the class
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
