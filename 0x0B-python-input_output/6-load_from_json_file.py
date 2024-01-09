#!/usr/bin/python3
""" Defines a function that creates an Obj from a JSON"""
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a JSON file

    Args:
        filename: textfile name

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
