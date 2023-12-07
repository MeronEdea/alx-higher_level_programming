#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = list(a_dictionary.keys())
    sorted_dictionary.sort()
    for i in sorted_dictionary:
        print("{}: {}".format(i, a_dictionary.get(i)))