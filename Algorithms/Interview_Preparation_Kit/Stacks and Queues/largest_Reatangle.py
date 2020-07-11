# Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

# There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by . If you join  adjacent buildings, they will form a solid rectangle of area .

# For example, the heights array . A rectangle of height  and length  can be constructed within the boundaries. The area formed is .

# Function Description

# Complete the function largestRectangle int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.

# largestRectangle has the following parameter(s):

# h: an array of integers representing building heights
# Input Format

# The first line contains , the number of buildings.
# The second line contains  space-separated integers, each representing the height of a building.

# Constraints

# Output Format

# Print a long integer representing the maximum area of rectangle formed.

# Sample Input

# 5
# 1 2 3 4 5
# Sample Output

# 9
# Explanation

# An illustration of the test case follows.
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    h.append(0)
    stack = []
    ans = float("-inf")
    for i,c in enumerate(h):
        if not stack or c>stack[-1][1]:
            stack.append((i,c))
        else:
            while stack and stack[-1][1]>=c:
                top=stack.pop()
                ans = max(ans,top[1]*(i-top[0]))
                left = top[0]
            if stack:
                stack.append((left,c))
            else:
                stack.append((0,c))
    
    return ans

def largestRectangle_(h):
    if len(h)==0:
        return 0
    elif len(h)==1:
        return h[0]
    elif len(h)==2:
        return max(min(h)*2,max(h))
    else:
        min_ind,min_v = -1,float("inf")
        for i,v in enumerate(h):
            if v<min_v:
                min_v = v
                min_ind = i
        return max(min_v*len(h),largestRectangle(h[:min_ind]),largestRectangle(h[min_ind+1:]))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
