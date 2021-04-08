#!/usr/bin/python3

def find_peak(list_of_integers):
    size = len(list_of_integers)
    for i in range(size):
        if i == 0:
            prev_n = 0
        else:
            prev_n = list_of_integers[i - 1]
        if i == size - 1:
            next_n = 0
        else:
            next_n = list_of_integers[i + 1]
        curr_n = list_of_integers[i]
        if  curr_n >= prev_n and curr_n >= next_n:
            return curr_n;
    return None
