#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def initd(arr,d):
    res = [0]*201
    for i in range(d):
        res[arr[i]]+=1
    return res

def accu(arr):
    res = arr[:]
    for i in range(1,len(res)):
        res[i] = res[i]+res[i-1]
    return res

def getMean(arr):
    length = arr[-1]
    if length%2==1:
        target = (length+1)//2
        for i,a in enumerate(arr):
            if a>=target:
                return i
    else:
        t1,t2 = length//2,length//2+1
        s1,s2 = -1,-1
        for i,a in enumerate(arr):
            if a>=t1 and s1==-1:
                s1 = i
            if a>=t2 and s2==-1:
                s2 = i
            if s1!=-1 and s2!=-1:
                break
        return (s1+s2)/2
    
def activityNotifications(expenditure, d):
    init_cnt_arr = initd(expenditure,d)
    cnt = 0
    for i in range(d,len(expenditure)):
        if i!=d:
            init_cnt_arr[expenditure[i-1]]+=1
            init_cnt_arr[expenditure[i-d-1]]-=1
        accu_arr = accu(init_cnt_arr)
        mean = getMean(accu_arr)
        if expenditure[i]>=2*mean:
            cnt+=1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
