#!/usr/bin/python3
"""
    Sends a request to the passed URL and displays the value of the
    X-Request-Id header variable
"""

from urllib import request
from sys import argv


if __name__ == '__main__':
    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
