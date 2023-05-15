#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for y in matrix:
            print(" ".join("{:d}".format(x) for x in y))
