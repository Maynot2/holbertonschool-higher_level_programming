#!/usr/bin/python3
"""
    Fetches https://intranet.hbtn.io/status using requests package
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = argv[1] if len(argv) > 1 else ""
    params = {'q': letter}
    resp = requests.post(url, params)
    try:
        json = resp.json()
        if json:
            print('[{}] {}'.format(json['id'], json['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
