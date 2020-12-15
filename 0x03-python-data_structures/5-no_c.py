#!/usr/bin/python3


def no_c(my_string):
    char_list = list(my_string)
    for i in range(len(char_list)):
        if char_list[i].lower() == "c":
            char_list[i] = ""
    return "".join(char_list)
