#!/usr/bin/python3
class Rectangle:
    def width(self, width):
        try:
            if not isinstance(width,int):
                raise TypeError("width must be an integer")
            elif width<0:
                raise ValueError("width must be >= 0")
            else:
                self.width = width
        except (TypeError, ValueError) as e:
            print(str(e))
    def height(self, height):
        try:
            if not isinstance(height,int):
                raise TypeError("height must be an integer")
            elif height<0:
                raise ValueError("height must be >= 0")
            else:
                self.height = height
        except (TypeError, ValueError) as e:
            print(str(e))
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
