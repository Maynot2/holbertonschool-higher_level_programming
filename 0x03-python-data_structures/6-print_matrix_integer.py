#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print("")
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print(row[i])
            else:
                print("{}".format(row[i]), end=" ")
