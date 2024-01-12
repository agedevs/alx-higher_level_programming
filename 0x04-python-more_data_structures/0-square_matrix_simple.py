#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    test_matrix = []
    for row in matrix:
        test_matrix.append([x ** 2 for x in row])
    return test_matrix
