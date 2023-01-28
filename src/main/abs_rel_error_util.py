from decimal import *

def absolute_error(orig, nxt):
    orig = Decimal(orig)
    nxt = Decimal(nxt)
    return abs(nxt - orig)

def relative_error(orig, nxt):
    orig = Decimal(orig)
    nxt = Decimal(nxt)
    return abs(nxt - orig) / orig
