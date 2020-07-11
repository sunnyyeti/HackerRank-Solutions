# You are planning production for an order. You have a number of machines that each have a fixed number of days to produce an item. Given that all the machines operate simultaneously, determine the minimum number of days to produce the required order.

# For example, you have to produce  items. You have three machines that take  days to produce an item. The following is a schedule of items produced:

# Day Production  Count
# 2   2               2
# 3   1               3
# 4   2               5
# 6   3               8
# 8   2              10
# It takes  days to produce  items using these machines.

# Function Description

# Complete the minimumTime function in the editor below. It should return an integer representing the minimum number of days required to complete the order.

# minimumTime has the following parameter(s):

# machines: an array of integers representing days to produce one item per machine
# goal: an integer, the number of items required to complete the order
# Input Format

# The first line consist of two integers  and , the size of  and the target production.
# The next line contains  space-separated integers, .

# Constraints

# Output Format

# Return the minimum time required to produce  items considering all machines work simultaneously.

# Sample Input 0

# 2 5
# 2 3
# Sample Output 0

# 6
# Explanation 0

# In  days  can produce  items and  can produce  items. This totals up to .

# Sample Input 1

# 3 10
# 1 3 4
# Sample Output 1

# 7
# Explanation 1

# In  minutes,  can produce  items,  can produce  items and  can produce  item, which totals up to .

# Sample Input 2

# 3 12
# 4 5 6
# Sample Output 2

# 20
# Explanation 2

# In  days  can produce  items,  can produce , and  can produce .
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the minTime function below.


def minTime(machines, goal):
    def issuccess(days):
        return sum(days//m*c for m, c in mac_cnt.items()) >= goal
    mac_cnt = Counter(machines)
    up = min(machines)*goal
    low = 0
    while low < up:
        mid = (low+up)//2
        if issuccess(mid):
            up = mid
        else:
            low = mid+1
    return up


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
