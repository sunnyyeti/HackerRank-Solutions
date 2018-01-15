#!/bin/python

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    keyboards.sort(reverse=True)
    drives.sort()
    d_start = 0
    max_sum = -1
    for k in xrange(len(keyboards)):
        d = d_start
        while d<len(drives):
            if keyboards[k]+drives[d]>s:
                d_start=d
                break
            else:
                if keyboards[k]+drives[d]>max_sum:
                    max_sum = keyboards[k]+drives[d]
                d+=1
        if d==len(drives):
            break
    return max_sum

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
#keyboards.sort(reverse=True)
drives = map(int, raw_input().strip().split(' '))
#drives.sort(reverse=True)
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
