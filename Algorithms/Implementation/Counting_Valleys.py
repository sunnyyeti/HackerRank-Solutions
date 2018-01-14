#!/bin/python

import sys

def countingValleys(n, s):
    # Complete this function
    level = 0
    cnt = 0
    for step in s:
        if step=='U':
            level+=1
            if level == 0:
                cnt += 1
        else:
            level -= 1
    return cnt

if __name__ == "__main__":
    n = int(raw_input().strip())
    s = raw_input().strip()
    result = countingValleys(n, s)
    print result
