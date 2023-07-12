#!/usr/bin/python3
"""
    Generates the first n rows of Pascal's triangle.
    :param n: The number of rows to generate.
    :type n: int
    :return: True if n >= 1, False otherwise.
    :rtype: bool
    """


def pascal_triangle(n):
    """Prints out n rows of Pascal's triangle.
    It returns False for failure and True for success"""
    triangle = []
    row = [1]
    k = [1]
    for x in range(max(n, 0)):
        triangle.append(row)
        row = list(map(lambda l, r: l + r, row + k, k + row))
    return triangle
