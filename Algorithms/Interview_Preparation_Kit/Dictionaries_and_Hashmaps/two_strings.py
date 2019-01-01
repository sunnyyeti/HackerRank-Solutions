#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def stringSet(s):
    res = set()
    return set(s)
def twoStrings(s1, s2):
    reference = stringSet(s2)
    for s in s1:
        if s in reference:
            return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

