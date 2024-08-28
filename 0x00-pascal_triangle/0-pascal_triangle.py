#!/usr/bin/python3
"""Triangle Triangle"""


def pascal_triangle(n):
    """Triangle"""
    if n <= 0:
        return []
    pasc = [[1]]
    for row_number in range(1, n):
        row = [1]
        for j in range(1, row_number):
            element = pasc[row_number - 1][j - 1] + pasc[row_number - 1][j]
            row.append(element)
        row.append(1)
        pasc.append(row)

    return pasc
