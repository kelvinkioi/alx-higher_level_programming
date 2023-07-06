#!/usr/bin/python3
"""Script for an add func"""


def add_integer(a, b=98):
    """Add function"""
    if a is None or not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if b is None or not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a + b)
