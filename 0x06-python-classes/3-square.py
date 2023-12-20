#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            if not isinstance(size,int):
                return TypeError("size must be an integer")
            elif size < 0:
                return ValueError("size must be >=0")
            else:
                self.__size = size
        except (TypeError, ValueError) as e:
            print(str(e))
    
    def area(self):
        return self.__size **2
