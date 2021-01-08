#!/usr/bin/python3
"""Contains function(s) to manipulate matrix"""


def raise_if_invalid_matrix(matrix):
    """Checks if matrix is valid and raises an error if it isn't"""

    if not matrix:
        raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')
    first_row = matrix[0]
    if not type(first_row) == list:
        raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')
    row_size = len(first_row)
    for row in matrix:
        if not type(row) == list:
            raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')
        if len(row) != row_size:
            raise TypeError('Each row of the matrix must have the same size')
        for elm in row:
            if type(elm) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')


def raise_if_invalid_divisor(divisor):
    """Checks if a divisor is valid and raises an error if it isn't"""

    if type(divisor) not in [float, int]:
        raise TypeError('div must be a number')
    if divisor == 0:
        raise ZeroDivisionError('division by zero')


def matrix_divided(matrix, div):
    """
        Divide all elements of a given matrix by a given divisor provided the
        matrix is correctly formatted
    """

    raise_if_invalid_matrix(matrix)
    raise_if_invalid_divisor(div)
    return [[round(elm / div, 2) for elm in row] for row in matrix]
