#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    maxh = -1
    maxcnt = 0
    for h in ar:
        if h > maxh:
            maxh = h
            maxcnt = 1
        elif h==maxh:
            maxcnt+=1
    return maxcnt

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)