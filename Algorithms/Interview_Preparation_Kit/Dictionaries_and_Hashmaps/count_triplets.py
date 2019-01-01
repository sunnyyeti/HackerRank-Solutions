#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = {}
    for a in arr:
        tmp_cnt = count.setdefault(a,[0,0,0]) ## number of a as first, second and third in geometric progression tuple
        if a/r in count:
            pre_cnt = list(count[a/r])
            tmp_cnt[0] += 1
            tmp_cnt[1] += pre_cnt[0]
            tmp_cnt[2] += pre_cnt[1]
        else:
            tmp_cnt[0]+=1
    total_cnt = 0
    for c in count:
        if c/(r*r) in count:
            total_cnt += count[c][2]
    return total_cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
