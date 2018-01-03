#!/bin/python

import sys

def migratoryBirds(n, ar):
    # Complete this function
    cnt =[0]*5
    for t in ar:
        cnt[t-1]+=1
    maxcnt = -1
    t = -1
    for i,c in enumerate(cnt):
        if c > maxcnt:
            maxcnt=c
            t = i
    return t+1

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)