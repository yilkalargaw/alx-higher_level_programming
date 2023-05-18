#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for i in matrix:
        sq_matrix.append(list(map(lambda j: j * j, i)))
    return sq_matrix
