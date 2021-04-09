#!/usr/bin/python3
"""
    Sends a request to the URL and displays the body of the response
    Handles HTTP errors
"""

from urllib import request, error
from sys import argv


if __name__ == '__main__':
    try:
        req = request.Request(argv[1])
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
