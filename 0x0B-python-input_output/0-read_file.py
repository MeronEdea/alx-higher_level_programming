#!/usr/bin/python3
""" Defines a function that reads a text file and prints it to stdout """


def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
