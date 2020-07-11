# In an array, , the elements at indices  and  (where ) form an inversion if . In other words, inverted elements  and  are considered to be "out of order". To correct an inversion, we can swap adjacent elements.

# For example, consider the dataset . It has two inversions:  and . To sort the array, we must perform the following two swaps to correct the inversions:

# Given  datasets, print the number of inversions that must be swapped to sort each dataset on a new line.

# Function Description

# Complete the function countInversions in the editor below. It must return an integer representing the number of inversions required to sort the array.

# countInversions has the following parameter(s):

# arr: an array of integers to sort .
# Input Format

# The first line contains an integer, , the number of datasets.

# Each of the next  pairs of lines is as follows:

# The first line contains an integer, , the number of elements in .
# The second line contains  space-separated integers, .
# Constraints

# Output Format

# For each of the  datasets, return the number of inversions that must be swapped to sort the dataset.

# Sample Input

# 2  
# 5  
# 1 1 1 2 2  
# 5  
# 2 1 3 1 2
# Sample Output

# 0  
# 4   
# Explanation

# We sort the following  datasets:

#  is already sorted, so there are no inversions for us to correct. Thus, we print  on a new line.
# We performed a total of  swaps to correct inversions.
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    if len(arr) in [0,1]:
        return arr,0
    arr1,inv1 = countInversions(arr[:len(arr)//2])
    arr2,inv2 = countInversions(arr[len(arr)//2:])
    i=j=0
    ans = inv1+inv2
    new_arr = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            new_arr.append(arr1[i])
            i+=1
        else:
            ans+=(len(arr1)-i)
            new_arr.append(arr2[j])
            j+=1
    while i<len(arr1):
        new_arr.append(arr1[i])
        i+=1
    while j<len(arr2):
        new_arr.append(arr2[j])
        j+=1
    return new_arr,ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)[1]

        fptr.write(str(result) + '\n')

    fptr.close()
