#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    res = {}
    for m in magazine:
        res[m] = res.setdefault(m,0)+1
    flag = "Yes"
    for n in note:
        res[n] = res.setdefault(n,0)-1
        if res[n]<0:
            flag = "No"
            break

    print(flag)

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
