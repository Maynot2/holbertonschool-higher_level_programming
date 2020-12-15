#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    cpy = my_list.copy()
    cpy.reverse()
    for num in cpy:
        print("{:d}".format(num))
