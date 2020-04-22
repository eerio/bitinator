#!/bin/python3
from requests import get

base = 'bitinator.net/'
http = 'http://'
https = 'https://'
sub = 'pawel.'  # non-existent subdomain
pat = 'agawa'  # non-existent path
www = 'www.'
tod = 'todo.'


for schema in (http, https):
    # base --303--> https+www+base
    resp = get(schema + base)
    assert len(resp.history) == 1
    assert resp.history[0].status_code == 303
    assert resp.url == https + www + base

# http+www+base --303--> https
resp = get(http + www + base)
assert len(resp.history) == 1
assert resp.history[0].status_code == 303
assert resp.url == https + www + base

# https+www+base --> https+www+base
resp = get(https + www + base)
assert len(resp.history) == 0
assert resp.url == https + www + base

