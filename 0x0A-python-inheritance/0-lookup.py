#!/usr/bin/python3
def lookup(obj):
    """ a function that returns the list of available attributes and
    methods of an object:

    Args:
        obj: instance of the class

    Returns:
        list object
    """

    return (dir(obj))
