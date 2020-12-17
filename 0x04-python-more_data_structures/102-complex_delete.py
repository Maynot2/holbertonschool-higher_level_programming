#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    keys = []
    for k, v in a_dictionary.items():
        if v == value:
            keys.append(k)
    for key in keys:
        a_dictionary.pop(key)
    return a_dictionary
