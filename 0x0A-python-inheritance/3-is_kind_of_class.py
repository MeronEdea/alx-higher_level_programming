#!/usr/bin/python3
"""defines a function that check an object"""


def is_kind_of_class(obj, a_class):
    """ Function that returns True/False if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
