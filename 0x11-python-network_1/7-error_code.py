#!/usr/bin/python3
"""
    Fetches https://intranet.hbtn.io/status using requests package
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    resp = requests.get(url)
    if resp.ok:
        print(resp.text)
    else:
        print('Error code: {}'.format(resp.status_code))
