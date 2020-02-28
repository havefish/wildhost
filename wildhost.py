'Checks wildcard domain names'

__version__ = '0.0.2'


import socket
from uuid import uuid1

import tldextract


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
            return s, c
    return s, None


def check_static(s, ws):
    for w in ws:
        if s.endswith(f'.{w}'):
            return s, w
    return s, None


def check_all(l):
    ws = set()
    
    for c in set(l):
        w = check_static(c, ws)
        if w:
            yield c, w
            continue
        
        w = check(c)
        if w:
            ws.add(w)
            
        yield c, w
