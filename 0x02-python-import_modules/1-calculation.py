#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    """
    program that imports functions from the file calculator_1.py
    does some Maths, and prints the result
    the functions are add sub mul and div
    """
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
