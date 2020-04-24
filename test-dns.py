#!/bin/python3
from requests import get
from requests.exceptions import ConnectionError

base = 'bitinator.net/'
http = 'http://'
https = 'https://'
sub = 'pawel.'  # non-existent subdomain
pat = 'agawa'  # non-existent path
www = 'www.'
tod = 'todo.'
dummy = 'a/b/c.php'

R = 303

def msg(check, n, out):print(check, 'expected: %d redirect(s), output url: %s...' % (n, out))
def ok():print('passed!')


def test(to_check, should_fail, is_red=False, out_url=''):
    msg(to_check, is_red, out_url)

    for dummy in ('', 'a/', 'a/b/', 'a/b/c.html'):
    #for dummy in ('',):
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

