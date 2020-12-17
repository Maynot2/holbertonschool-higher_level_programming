#!/usr/bin/python3


def common_elements(set_1, set_2):
    if set_1 is not None or set_2 is not None:
        return {x for x in set_1 if x in set_2}
