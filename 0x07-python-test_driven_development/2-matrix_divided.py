#!/usr/bin/python3
"""This module is composed by a function"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    len_e = 0

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len_e != 0 and len(elems) != len_e:
            raise TypeError("Each row of the matrix must have the same size")

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
