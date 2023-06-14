#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = [[j ** 2 for j in i] for i in matrix]
    return my_matrix
