#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    Quotient = []
    try:
        for i in range(list_length):
            try:
                dividend = my_list_1[i]
                divisor = my_list_2[i]
                try:
                    division = dividend / divisor
                    Quotient.append(division)
                except ZeroDivisionError:
                    Quotient.append(0)
                    print("division by 0")
                except:
                    Quotient.append(0)
                    print("wrong type")
            except IndexError:
                Quotient.append(0)
                print("out of range")
    except:
        pass
    return Quotient
