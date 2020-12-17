#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    if set_1 is not None or set_2 is not None:
        diff1 = [x for x in set_1 if x not in set_2]
        diff2 = [x for x in set_2 if x not in set_1]
        return set(diff1 + diff2)
