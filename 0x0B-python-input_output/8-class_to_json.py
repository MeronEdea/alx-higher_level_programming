#!/usr/bin/python3
""" Defines a function returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for
JSON serialization of an object
"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    disc = {}
    if hasattr(obj, "__dict__"):
        disc = obj.__dict__.copy()
    return disc
