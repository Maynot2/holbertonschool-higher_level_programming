#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if my_list:
        if 0 <= idx < len(my_list):
            return my_list[:idx] + my_list[idx+1:]
        else:
            return my_list
