#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value), end='')
    except:
        return False
    return True

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed = 0
    while i < x:
        if safe_print_integer(my_list[i]):
            printed += 1
        if i + 1 == x:
            print();
        i += 1
    return printed
