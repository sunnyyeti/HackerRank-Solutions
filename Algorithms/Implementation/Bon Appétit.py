#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    total = sum(ar)
    should = (total-ar[k])/2
    if b==should:
        return "Bon Appetit"
    else:
        return b-should

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)