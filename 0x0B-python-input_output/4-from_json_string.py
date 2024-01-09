#!/usr/bin/python3
""" Defines a function that returns an object"""
import json


def from_json_string(my_str):
    """ function that returns an object represented by a JSON string

    Args:
        my_str: JSON representation

    """
    return json.loads(my_str)
