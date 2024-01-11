#!/usr/bin/python3
"""Defines a module that contains a function"""


def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size of the square printed

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
