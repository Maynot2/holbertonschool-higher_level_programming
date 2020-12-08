#!/usr/bin/python3


def _islower(c):
    return 97 <= ord(c) <= 122


def uppercase(str):
    str += "\n"
    for char in str[:]:
        if _islower(char):
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print(char, end="")
