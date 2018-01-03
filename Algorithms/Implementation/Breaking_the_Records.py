#!/bin/python

import sys

def breakingRecords(score):
    # Complete this function
    min_s = max_s = score[0]
    min_c = 0
    max_c = 0
    for i in xrange(1,len(score)):
        if score[i]>max_s:
            max_s = score[i]
            max_c +=1
        if score[i]<min_s:
            min_s = score[i]
            min_c += 1
    return max_c,min_c

if __name__ == "__main__":
    n = int(raw_input().strip())
    score = map(int, raw_input().strip().split(' '))
    result = breakingRecords(score)
    print " ".join(map(str, result))