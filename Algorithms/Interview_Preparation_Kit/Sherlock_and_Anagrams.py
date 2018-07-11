#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    s_list = list(s)
    res = {}
    cnt = 0
    for i,s in enumerate(s_list):
        for j in range(i+1):
            tmp = s_list[j:i+1]
            tmp.sort()
            tmp = tuple(tmp)
            cnt += res.setdefault(tmp,0)
            res[tmp] = res.setdefault(tmp,0)+1
    return cnt
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

