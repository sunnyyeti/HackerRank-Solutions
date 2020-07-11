#!/bin/python

import sys

def solve(grades):
    # Complete this function
    return [g if (g<38 or ((g/5+1)*5-g)>=3) else 5*(g/5+1) for g in grades]

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))