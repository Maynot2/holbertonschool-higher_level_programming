#!/usr/bin/python3
"""
    Fetches https://intranet.hbtn.io/status
"""

from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        resp = response.read()
        content = resp.decode('utf-8')
        body = '''\
Body response:
    - type: {}
    - content: {}
    - utf8 content: {}'''.format(type(resp), resp, content)
        print(body)
