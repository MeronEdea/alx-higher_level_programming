#!/usr/bin/python3
def is_same_class(obj, a_class):
    """function that returns True/False if the object is exactly an instance of the specified class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return type(obj) is a_class
