#!/usr/bin/python3
"""defines a function for pascal triangle"""


def pascal_triangle(n):
    if n<=0:
        return []
    
    pascangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascangle[i-1][j-1] + pascangle[i-1][j])
        row.append(1)
        pascangle.append(row)

    return pascangle
