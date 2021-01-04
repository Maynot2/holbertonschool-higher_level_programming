#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    if my_list:
        while i < x:
            try:
                print(my_list[i], end="")
                if i + 1 == x:
                    print()
                i += 1
            except:
                print()
                break
    if i == 0:
        print()
    return i
