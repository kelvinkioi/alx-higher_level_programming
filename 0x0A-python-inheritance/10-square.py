#!/usr/bin/python3
""" subclass Square of the class rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square -  inheritance form rectangle
    """

    def __init__(self, size):
        """
        Initializes a new square.
        Args:
        size (int): The size of the new square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
