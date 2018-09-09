"""
You are given an unordered array of unique integers incrementing from . You can swap any two elements a limited number of times. Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.

For example, if  and the maximum swaps , the following arrays can be formed by swapping the  with the other elements:

[2,1,3,4]
[3,2,1,4]
[4,2,3,1]
The highest value of the four (including the original) is . If , we can swap to the highest possible value: .

Function Description

Complete the largestPermutation function in the editor below. It must return an array that represents the highest value permutation that can be formed.

largestPermutation has the following parameter(s):

k: an integer that represents the limit of swaps
arr: an array of integers
Input Format

The first line contains two space-separated integers  and , the length of  and the maximum swaps that can be performed. The second line contains  unique space-separated integers  where .

Constraints

 

Output Format

Print the lexicographically largest permutation you can make with at most  swaps. 
Sample Input 0

5 1
4 2 3 5 1
Sample Output 0

5 2 3 4 1
Explanation 0

You can swap any two numbers in  and see the largest permutation is 

Sample Input 1

3 1
2 1 3
Sample Output 1

3 1 2
Explanation 1

With 1 swap we can get ,  and . Of these,  is the largest permutation.

Sample Input 2

2 1
2 1
Sample Output 2

2 1
Explanation 2

We can see that  is already the largest permutation. We don't make any swaps."""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
        new_arr = arr[::]
        new_arr.sort()
        v2ind = {v: i for i, v in enumerate(arr)}
        cnt = 0
        i = 0
        while cnt<k and i<len(arr):
            max_v = new_arr[-1-i]
            max_ind = v2ind[max_v]
            if max_ind != i:
                arr[i], arr[max_ind] = arr[max_ind], arr[i]
                v2ind[arr[max_ind]] = v2ind[arr[i]]
                cnt+=1
            i+=1
        return arr
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
