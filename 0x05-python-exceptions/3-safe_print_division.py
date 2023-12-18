#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        Quotient = a / b
    except ZeroDivisionError:
        Quotient = None
    finally:
        print("Inside result: {}".format(Quotient))
        return Quotient
