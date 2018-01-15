#!/bin/python

import sys

def catAndMouse(x, y, z):
    # Complete this function
    if abs(x-z)<abs(y-z):
        return ["Cat","A"]
    elif abs(x-z)>abs(y-z):
        return ["Cat","B"]
    else:
        return ["Mouse","C"]

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        x, y, z = raw_input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print " ".join(map(str, result))
