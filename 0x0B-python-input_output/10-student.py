#!/usr/bin/python3
""" Defines student class"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            dict = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        dict[satr] = obj[satr]
            return dict

        return obj
