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

<<<<<<< HEAD
def test(to_check, should_fail, is_red=False, out_url=''):
    msg(to_check, is_red, out_url)

    #for dummy in ('', 'a/', 'a/b/', 'a/b/c.html'):
    for dummy in ('',):
        print('real url checked:', to_check + dummy)
        if should_fail:
            try:
                resp = get(to_check + dummy)
                raise AssertionError("Didn't fail, but should have")
            except ConnectionError:
                ok()
                continue
        else:
            resp = get(to_check + dummy)

        
        #if len(resp.history) != int(is_red):
        #    raise AssertionError(str(resp.history), resp.url, 'wrong n of redirects')
        #if is_red: assert resp.history[0].status_code == R
        if resp.url != out_url + dummy:
            raise AssertionError(resp.url, '!=', out_url + dummy)
        ok()

typical = https + www + base
test(http+base, False, 1, typical)
test(https+base, False, 1, typical)
test(http+www+base, False, 1, typical)
test(https+www+base, False, 0, typical)
test(http+tod+base, False, 1, https+tod+base)
test(https+tod+base, False, 0, https+tod+base)
test(http+sub+base, True)
test(https+sub+base, True)
=======
# https+www+base --> https+www+base
resp = get(https + www + base)
assert len(resp.history) == 0
assert resp.url == https + www + base
>>>>>>> test

