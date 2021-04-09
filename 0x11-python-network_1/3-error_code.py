#!/usr/bin/python3
"""
    Sends a request to the URL and displays the body of the response
    Handles HTTP errors
"""

import urllib
from sys import argv


if __name__ == '__main__':
    req = urllib.request.Request(argv[1])
    try:
        response = urllib.request.urlopen(req)
        print(response.read().decode('utf-8'))
    except urlib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
