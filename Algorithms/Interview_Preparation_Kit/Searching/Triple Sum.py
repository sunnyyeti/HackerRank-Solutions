# Given  arrays  of different sizes, find the number of distinct triplets  where  is an element of , written as , , and , satisfying the criteria: .

# For example, given  and , we find four distinct triplets: .

# Function Description

# Complete the triplets function in the editor below. It must return the number of distinct triplets that can be formed from the given arrays.

# triplets has the following parameter(s):

# a, b, c: three arrays of integers .
# Input Format

# The first line contains  integers , the sizes of the three arrays.
# The next  lines contain space-separated integers numbering  respectively.

# Constraints



# Output Format

# Print an integer representing the number of distinct triplets.

# Sample Input 0

# 3 2 3
# 1 3 5
# 2 3
# 1 2 3
# Sample Output 0

# 8 
# Explanation 0

# The special triplets are  .

# Sample Input 1

# 3 3 3
# 1 4 5
# 2 3 3
# 1 2 3
# Sample Output 1

# 5 
# Explanation 1

# The special triplets are 

# Sample Input 2

# 4 3 4
# 1 3 5 7
# 5 7 9
# 7 9 11 13
# Sample Output 2

# 12
# Explanation 2

# The special triplets are .

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.


def lower_bound(arr, tar):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] <= tar:
            start = mid+1
        else:
            end = mid - 1
    return end


def upper_bound(arr, tar):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] < tar:
            start = mid+1
        else:
            end = mid - 1
    return start


def triplets(a, b, c):
    a = sorted(set(a))
    b = set(b)
    c = sorted(set(c))
    ans = 0
    for v in b:
        low = lower_bound(a, v)
        high = lower_bound(c, v)
        #print(v,low,high)
        ans += (low+1)*(high+1)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
