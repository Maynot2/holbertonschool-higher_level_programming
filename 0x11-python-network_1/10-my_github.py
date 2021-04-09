#!/usr/bin/python3
"""
    sends a POST request to http://0.0.0.0:5000/search_user with a letter as
    parameter.
"""

import requests
from sys import argv


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    url = 'https://api.github.com/users/{}'.format(user)
    pars = {'token': passwd}
    resp = requests.get(url, params=pars)
    try:
        json = resp.json()
        print('{}'.format(json['id']))
    except:
        print('Not a valid JSON')
