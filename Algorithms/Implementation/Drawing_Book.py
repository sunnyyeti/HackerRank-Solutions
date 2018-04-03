#!/bin/python

import sys
import math
def solve(n, p):
    # Complete this function
    return int(min(math.ceil((p-1)/2.0),math.ceil((n/2*2-p)/2.0)))

n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print(result)