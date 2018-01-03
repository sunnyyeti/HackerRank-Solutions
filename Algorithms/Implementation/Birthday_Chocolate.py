#!/bin/python

import sys

def solve(n, s, d, m):
    # Complete this function
    ini_sum = sum(s[:m])
    cnt = 1 if ini_sum==d else 0
    for index in xrange(m,n):
        ini_sum += s[index] - s[index-m]
        if ini_sum == d:
            cnt += 1
    return cnt

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)