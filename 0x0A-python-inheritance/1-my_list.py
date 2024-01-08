#!/usr/bin/python3
class MyList(list):
    """ Class MyList that inherits from list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        ascending_sorted = self.copy()
        ascending_sorted.sort()
        print(ascending_sorted)
