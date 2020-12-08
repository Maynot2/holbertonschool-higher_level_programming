#!/usr/bin/python3


def islower(c):
    return 97 <= ord(c) <= 122


def uppercase(str):
    str += "\n"
    for char in str[:]:
        if islower(char):
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
