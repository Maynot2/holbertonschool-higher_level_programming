#!/usr/bin/python3
"""
    list 10 commits (from the most recent to oldest) of the repository “rails”
    by the user “rails”
"""

import requests
from sys import argv

if __name__ == '__main__':
    sha = argv[1]
    repo = argv[2]
    h = {'Accept': 'application/vnd.github.v3+json'}
    u = 'https://api.github.com/repos/{}/{}/commits'.format(sha, repo)
    resp = requests.get(url=u, params={'per_page': 10}, headers=h)
    json = resp.json()
    for commit in json:
        print('{}: {}'.format(commit.get('sha'),
              commit.get('commit').get('author').get('name')))
