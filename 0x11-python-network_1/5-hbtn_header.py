#!/usr/bin/python3
"""
    Fetches https://intranet.hbtn.io/status using requests package
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    resp = requests.get(url)
    print(resp.headers.get('x-request-id')
