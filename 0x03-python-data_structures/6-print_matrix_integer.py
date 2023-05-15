#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for i in [[str(x) for x in row] for row in matrix]:
            print(" ".join(i))
