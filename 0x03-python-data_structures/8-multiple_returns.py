#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence != None:
        str_len = len(sentence)
        if str_len > 0:
            return (len(sentence), sentence[0])
        else:
            return (0, None)
