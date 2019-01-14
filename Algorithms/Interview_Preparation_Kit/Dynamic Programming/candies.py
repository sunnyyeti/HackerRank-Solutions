# Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.

# For example, assume her students' ratings are [4, 6, 4, 5, 6, 2]. She gives the students candy in the following minimal amounts: [1, 2, 1, 2, 3, 1]. She must buy a minimum of 10 candies.

# Function Description

# Complete the candies function in the editor below. It must return the minimum number of candies Alice must buy.

# candies has the following parameter(s):

# n: an integer, the number of children in the class
# arr: an array of integers representing the ratings of each student
# Input Format

# The first line contains an integer, , the size of . 
# Each of the next  lines contains an integer  indicating the rating of the student at position .

# Constraints

# Output Format

# Output a single line containing the minimum number of candies Alice must buy.

# Sample Input 0

# 3
# 1
# 2
# 2
# Sample Output 0

# 4
# Explanation 0

# Here 1, 2, 2 is the rating. Note that when two children have equal rating, they are allowed to have different number of candies. Hence optimal distribution will be 1, 2, 1.

# Sample Input 1

# 10
# 2
# 4
# 2
# 6
# 1
# 7
# 8
# 9
# 2
# 1
# Sample Output 1

# 19
# Explanation 1

# Optimal distribution will be 

# Sample Input 2

# 8
# 2
# 4
# 3
# 5
# 2
# 6
# 4
# 5
# Sample Output 2

# 12
# Explanation 2

# Optimal distribution will be .

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n,arr):
    minimum_inds = [-1]
    val = [1]*len(arr)
    def expand_left(ind,end,arr,val):
        ind = ind-1
        while ind>end and arr[ind]>arr[ind+1]:
            val[ind] = max(val[ind+1]+1,val[ind])
            ind-=1
    def expand_right(ind,end,arr,val):
        ind = ind+1
        while ind<end and arr[ind]>arr[ind-1]:
            val[ind] = max(val[ind-1]+1,val[ind])
            ind+=1

    for i,a in enumerate(arr):
        if (i==0 and arr[i]<=arr[i+1]) or (i==len(arr)-1 and arr[i]<=arr[i-1]):
            minimum_inds.append(i)
        if (0<i<len(arr)-1 and arr[i]<=arr[i+1] and arr[i]<=arr[i-1]):
            minimum_inds.append(i)
    minimum_inds.append(len(arr))
    for ind in range(1,len(minimum_inds)-1):
        expand_left(minimum_inds[ind],minimum_inds[ind-1],arr,val)
        expand_right(minimum_inds[ind],minimum_inds[ind+1],arr,val)
    return sum(val)
        
def candies_recursive(n, arr):
    arr = [float("inf")]+arr+[float("inf")]
    val = [0]*len(arr)
    for i in range(1,len(arr)-1):
        if val[i]==0:
            helper(arr,val,i)
    return sum(val)

def helper(arr,val,ind):
    if val[ind]!=0:
        return val[ind]
    if arr[ind]<=arr[ind-1] and arr[ind]<=arr[ind+1]:
        val[ind]=1
        return val[ind]
    if arr[ind]>arr[ind-1] and arr[ind]>arr[ind+1]:
        val[ind] = max(helper(arr,val,ind-1),helper(arr,val,ind+1))+1
        return val[ind]
    if arr[ind]>arr[ind-1]:
        val[ind]=helper(arr,val,ind-1)+1
        return val[ind]
    else:
        val[ind]=helper(arr,val,ind+1)+1
        return val[ind]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
