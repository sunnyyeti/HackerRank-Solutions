#!/bin/python

import sys

def pickingNumbers(a):
    # Complete this function
    res = {}
    for v in a:
        res[v] = res.setdefault(v,0)+1
    ll = 0
    for i in a:
        max_cnt = max(res.setdefault(i,0)+res.setdefault(i+1,0),res.setdefault(i,0)+res.setdefault(i-1,0))
        if max_cnt>ll:
            ll = max_cnt
    return ll
if __name__ == "__main__":
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = pickingNumbers(a)
    print result

