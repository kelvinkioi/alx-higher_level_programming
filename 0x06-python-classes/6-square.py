#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """The representation of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ initializes the size
        of the square.
        args:
        size: is the size of the sqaure
        position: tuple of two positive integers"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """Class method that returns
        the area of the sqaure"""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrives the private instance of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """A property setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(end=' ')
            for i in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        """ retrieves the private instance of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ A property setter for position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) or i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
