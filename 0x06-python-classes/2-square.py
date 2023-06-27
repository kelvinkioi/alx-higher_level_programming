#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """The representation of a square"""

    def __init__(self, size=0):
        """__init__ initializes the size
        of the square.
        size, is the size of the sqaure"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
