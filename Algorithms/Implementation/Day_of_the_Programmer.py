#!/bin/python

import sys


def solve(year):
    # Complete this function
    years = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year<=1917:
        if year%4==0:
            years[1]=29
    elif year==1918:
        years[1]=15
    else:
        if (year%400==0) or (year%4==0 and not year%100==0):
            years[1] = 29
    total = 0
    for i, days in enumerate(years):
        total+=days
        if total>=256:
            d = days-total+256
            return "%02d.%02d.%04d"%(d,i+1,year)


year = int(raw_input().strip())
result = solve(year)
print(result)