#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for k in i:
            print("{:d}".format(k), end=' ' if i.index(k) < len(i) - 1 else '')
        print()
