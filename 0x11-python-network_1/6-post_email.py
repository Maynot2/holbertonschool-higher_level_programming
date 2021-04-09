#!/usr/bin/python3
"""
    Fetches https://intranet.hbtn.io/status using requests package
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    params = {'email': email}
    resp = requests.post(url, params)
    print(resp.text)
