#!/usr/bin/python3
            print(response.read().decode('utf-8'))
"""
    Fetches https://intranet.hbtn.io/status
"""

from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        resp = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(resp)))
        print('\t- content: {}'.format(resp))
        print('\t- utf8 content: {}'.format(resp.decode('utf-8')))
