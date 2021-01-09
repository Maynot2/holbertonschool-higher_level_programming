#!/usr/bin/python3
"""This module contains function to compute calculations on Matrix
"""


def is_rectangle(matrix):
    """Tests if matrix is a rectangle (all rows are the same length...)
    """
    base_len = len(matrix[0])
    for row in matrix:
        if len(row) != base_len:
            return False
    return True


def matrix_mul(m_a, m_b):
        """Multiplies matrix m_a with matrix m_b when compatible
        """
        if type(m_a) is not list:
            raise TypeError('m_a must be a list')
        if type(m_b) is not list:
            raise TypeError('m_b must be a list')
        if False in [isinstance(elm, list) for elm in m_a]:
            raise TypeError('m_a must be a list of lists')
        if False in [isinstance(elm, list) for elm in m_b]:
            raise TypeError('m_b must be a list of lists')
        if not m_a or False in [not not elm for elm in m_a]:
            raise ValueError('m_a can\'t be empty')
        if not m_b or False in [not not elm for elm in m_b]:
            raise ValueError('m_b can\'t be empty')
        if True in [type(elm) not in [float, int] for elm in sum(m_a, [])]:
            raise TypeError('m_a should contain only integers or floats')
        if True in [type(elm) not in [float, int] for elm in sum(m_b, [])]:
            raise TypeError('m_b should contain only integers or floats')
        if not is_rectangle(m_a):
            raise TypeError('each row of m_a must be of the same size')
        if not is_rectangle(m_b):
            raise TypeError('each row of m_b must be of the same size')
        if len(m_a[0]) != len(m_b):
            raise ValueError('m_a and m_b can\'t be multiplied')

        result = [[0 for y in range(len(m_b[0]))] for x in range(len(m_a))]

        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    result[i][j] += m_a[i][k] * m_b[k][j]

        return result

if __name__ == '__main__':
    print(matrix_mul([[1, 2]], [[1, 2, 3], [4, 5, 6]]))
