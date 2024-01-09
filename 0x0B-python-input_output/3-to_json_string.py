#!/usr/bin/python3
""" Defines a function that returns JSON """
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object (string)

    Args:
        my_obj: object

    """
    return json.dumps(my_obj)
