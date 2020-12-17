#!/usr/bin/python3


def best_score(a_dictionary):
    best = "None"
    best_score = 0
    if a_dictionary:
        for name, score in a_dictionary.items():
            if score > best_score:
                best = name
                best_score = score
    return best
