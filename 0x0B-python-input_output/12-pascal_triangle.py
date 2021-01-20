#!/usr/bin/python3
"""Implementation of the famous pascal triangle representation"""


def pascal_triangle(n):
    """Returns a pascal triangle of n rows"""
    triangle = []
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if j == 0 or j == i - 1:
                row.append(1)
            else:
                row.append(triangle[i - 2][j - 1] + triangle[i - 2][j])
        triangle.append(row)
    return triangle
