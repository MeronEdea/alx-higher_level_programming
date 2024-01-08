#!/usr/bin/python3
"""defines inherited class"""


class MyList(list):
    """implements sorting for buiult-in list class"""

    def print_sorted(self):
        """ Method that prints the sorted list """
        ascending_sorted = self.copy()
        ascending_sorted.sort()
        print(ascending_sorted)
