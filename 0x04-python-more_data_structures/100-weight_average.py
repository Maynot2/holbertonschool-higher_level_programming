#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    dictionary = dict(my_list)
    total = 0
    for k, v in dictionary.items():
        total += k * v
    return total / sum(dictionary.values())
