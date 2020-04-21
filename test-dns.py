#!/bin/python3
from requests import get

base = 'bitinator.net/'
http = 'http://'
https = 'https://'
sub = 'pawel.'
pat = 'agawa'
www = 'www.'

red = 303

# check if naked resolves to https + www
for resp in (get(http + base), get(https + base)):
    print(resp.history)
    assert len(resp.history) == 1
    assert resp.history[0].status_code == red
    assert resp.url == https + www + base

print(get("http://bitinator.net").history)
"https://bitinator.net"

"http://www.bitinator.net"
"https://www.bitinator.net"

"http://www.bitinator.net"
"https://www.bitinator.net"

"http://www.bitinator.net/pawel"
"https://www.bitinator.net/pawel"

"http://pawel.bitinator.net"
"https://pawel.bitinator.net"
"http://pawel.bitinator.net/agawa"
"https://pawel.bitinator.net/agawa"


