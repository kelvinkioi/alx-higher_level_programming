#!/usr/bin/python3
"""matrix function"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    ke = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    l = len(matrix[0])
    n = []
    for i in range(len(matrix)):
        if l != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
        n.append([])
        for j in matrix[i]:
            if not isinstance(j, float) and not isinstance(j, int):
                raise TypeError(ke)
            n[i].append(round(j / div, 2))
    return n
