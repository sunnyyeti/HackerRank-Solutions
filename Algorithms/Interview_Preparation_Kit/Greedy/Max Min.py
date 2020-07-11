# You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

# Where:
# - max denotes the largest integer in 
# - min denotes the smallest integer in 

# As an example, consider the array  with a  of . Pick any two elements, test .

# Testing for all pairs, the solution  provides the minimum unfairness.

# Note: Integers in  may not be unique.

# Function Description

# Complete the maxMin function in the editor below. It must return an integer that denotes the minimum possible value of unfairness.

# maxMin has the following parameter(s):

# k: an integer, the number of elements in the array to create
# arr: an array of integers .
# Input Format

# The first line contains an integer , the number of elements in array .
# The second line contains an integer .
# Each of the next  lines contains an integer  where .

# Constraints




# Output Format

# An integer that denotes the minimum possible value of unfairness.

# Sample Input 0

# 7
# 3
# 10
# 100
# 300
# 200
# 1000
# 20
# 30
# Sample Output 0

# 20
# Explanation 0

# Here ; selecting the  integers , unfairness equals

# max(10,20,30) - min(10,20,30) = 30 - 10 = 20
# Sample Input 1

# 10
# 4
# 1
# 2
# 3
# 4
# 10
# 20
# 30
# 40
# 100
# 200
# Sample Output 1

# 3
# Explanation 1

# Here ; selecting the  integers , unfairness equals

# max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3
# Sample Input 2

# 5
# 2
# 1
# 2
# 1
# 2
# 1
# Sample Output 2

# 0
# Explanation 2

# Here .  or  give the minimum unfairness of .
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    ans = float("inf")
    for i in range(len(arr)-k+1):
        ans = min(ans,arr[i+k-1]-arr[i])
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
