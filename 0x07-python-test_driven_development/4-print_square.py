#!/usr/bin/python3
"""Square func"""


def print_square(size):
    """function that prints a square with the character #"""
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for i in range(size):
            print('#', end='')
        print()
