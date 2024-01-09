#!/usr/bin/python3
""" Defines student class"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method retrieves a dictionary representation"""
        return self.__dict__.copy()
