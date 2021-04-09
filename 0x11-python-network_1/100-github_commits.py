#!/usr/bin/python3
"""
    sends a POST request to http://0.0.0.0:5000/search_user with a letter as
    parameter.
"""

import requests
from sys import argv

if __name__ == '__main__':
    sha = argv[1]
    repo = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sha, repo)
    resp = requests.get(url, params={'per_page': 10})
    json = resp.json()
    for commit in json:
        print('{}: {}'.format(commit.get('sha'),
              commit.get('commit').get('author').get('name')))
