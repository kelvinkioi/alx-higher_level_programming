#!/usr/bin/python3
if __name__ == "__main__":
    """
    program that imports functions from the file calculator_1.py
    does some Maths, and prints the result
    the functions are add sub mul and div
    """
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
