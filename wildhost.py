'Checks wildcard domain names'

__version__ = '0.0.2'


import socket
from uuid import uuid1

import tldextract

ws = set()

def resolves(s):
    try:
        socket.gethostbyname(s)
    except Exception:
        return False
    return True


def gen(s):
    r = tldextract.extract(s)

    d = f'{r.domain}.{r.suffix}'
    
    yield d
    
    words = r.subdomain.split('.')
        
    for i in range(len(words)):
        prefix = '.'.join(words[-i-1:])
        yield f'{prefix}.{d}'


def resolves_random(s):
    return resolves(f'{uuid1().hex}.{s}')


def check(s):
    for c in gen(s):
        if resolves_random(c):
            return c


def check_static(s, ws):
    for w in ws:
        if s.endswith(f'.{w}'):
            return w


def check_cached(s):
    w = check_static(s, ws)
    if w:
        return w

    w = check(s)
    if not w:
        return

    ws.add(w)
    return w
