#!/usr/bin/python3
def magic_string(like_static={'count': 0}):
    like_static['count'] += 1
    return ("Holberton, " * like_static['count'])[:-2]
