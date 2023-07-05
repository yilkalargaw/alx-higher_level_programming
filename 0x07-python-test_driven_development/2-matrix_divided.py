#!/usr/bin/python3
"""
This module is called 'matrix_divided'

It contains 1 function called 'matrix_divided'
It divides all elements in the matrix
"""


def matrix_divided(matrix, div):
    """This is the function that returns the division of 2 lists
    Args:
        matrix: matrix is 1st parameter
        div: 2nd parameter which divides the matrix
    Return:
        the divided elements of the matrix
    """
    err_msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_msg2 = "division by zero"
    err_msg3 = "division by zero"
    err_msg4 = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(err_msg1)

    mat = len(matrix[0])
    if len(matrix) == 0:
        raise TypeError(err_msg1)
    if mat == 0:
        raise TypeError(err_msg1)

    if div == 0:
        raise ZeroDivisionError(err_msg2)
    elif type(div) is not int and type(div) is not float:
        raise TypeError(err_msg3)

    for l in matrix:
        if type(l) is not list:
            raise TypeError(err_msg1)
        if len(l) is not mat:
            raise TypeError(err_msg4)

        for i in l:
            if type(i) is not int and type(i) is not float:
                raise TypeError(err_msg1)

    return ([[round(j / div, 2) for j in z] for z in matrix])
