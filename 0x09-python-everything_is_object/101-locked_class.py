#!/usr/bin/python3
"""Defines a class: LockedClass"""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes,
    and creates only if new instance attribute is called first_name
    """

    __slots__ = ["first_name"]
