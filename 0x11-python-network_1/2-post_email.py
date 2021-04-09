#!/usr/bin/python3
"""
    Sends a request to the passed URL and displays the value of the
    X-Request-Id header variable
"""

from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    data = parse.urlencode({'email': argv[2]})
    data = data.encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
