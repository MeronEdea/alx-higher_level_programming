#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for item in my_list:
            print(item, end="")
    except:
        pass
