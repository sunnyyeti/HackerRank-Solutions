#!/bin/python

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    divs = [0]*k
    cnt = 0
    for a in ar:
        divs[a%k]+=1
    for i in xrange(k/2+1):
        if i == (k-i)%k:
            cnt += divs[i]*(divs[i]-1)/2
        else:
            cnt += divs[i]*divs[k-i]
    return cnt

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)