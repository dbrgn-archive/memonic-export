# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals
import os
import sys
import json
import requests


# Helper stuff

def env(key):
    try:
        return os.environ[key]
    except KeyError:
        print('Please set the {key} environment variable.'.format(key=key))
        sys.exit(-1)

PY3 = sys.version_info[0] == 3

# Setup

USERNAME = env('MEMONIC_USER')
PASSWORD = env('MEMONIC_PASS')
API_KEY = env('MEMONIC_API_KEY')

session = requests.Session()
session.auth = (USERNAME, PASSWORD)
session.headers.update({'Accept': 'application/json'})

ENCODING = sys.stdout.encoding if hasattr(sys.stdout, 'encoding') else 'utf8'

URL = 'https://api.memonic.com/v2/users/{user_id}/{resource}?apikey={api_key}'

# Get the User ID

print('Getting the user_id...')
r = session.get('https://api.memonic.com/v2/users?apikey={api_key}'.format(api_key=API_KEY))
r.raise_for_status()
data = r.json()
user_id = data['users'][0]['id']

# Fetch Sets

print('Fetching sets...')
r = session.get(URL.format(resource='sets', user_id=user_id, api_key=API_KEY))
r.raise_for_status()
data = r.json()
with open('memonic_sets.json', 'w') as outfile:
    outfile.write(json.dumps(data['sets'], indent=2))

# Fetch Groups

print('Fetching groups...')
r = session.get(URL.format(resource='groups', user_id=user_id, api_key=API_KEY))
r.raise_for_status()
data = r.json()
with open('memonic_groups.json', 'w') as outfile:
    outfile.write(json.dumps(data['groups'], indent=2))

# Fetch Notes

print('Fetching notes...')
r = session.get(URL.format(resource='items', user_id=user_id, api_key=API_KEY))
r.raise_for_status()
data = r.json()
assert data['pagination']['pagesize'] == -1, \
        'Items resource returned multiple pages. This script cannot deal with that yet.'

notes = []
for item in data['items']:
    r = session.get(item['href'])
    r.raise_for_status()
    itemdata = r.json()
    notes.append(itemdata)
    msg = 'Fetched item "{title}"'.format(title=itemdata['data']['title'])
    if not PY3:
        msg = msg.encode(ENCODING, 'replace')
    print(msg)
with open('memonic_notes.json', 'w') as outfile:
    outfile.write(json.dumps(notes, indent=2))

print('Done.')
