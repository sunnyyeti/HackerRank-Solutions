#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(queries):
    cnt = {}
    cnt_r = {}
    res = []
    for q in queries:
        op = q[0]
        num = q[1]
        if op==1:
            pre_cnt = cnt.setdefault(num,0)
            cnt[num] = pre_cnt+1
            get_set = cnt_r.setdefault(pre_cnt+1,set())
            get_set.add(num)
            if pre_cnt!=0:
                get_set = cnt_r[pre_cnt]
                get_set.remove(num)
        elif op==2:
            pre_cnt = cnt.setdefault(num,0)
            cnt[num] = max(pre_cnt-1,0)
            if pre_cnt!=0:
                get_set = cnt_r[pre_cnt]
                get_set.remove(num)
            if cnt[num]!=0:
                get_set = cnt_r[cnt[num]]
                get_set.add(num)
        else:
            if num in cnt_r and len(cnt_r[num])>0:
                res.append(1)
            else:
                res.append(0)
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = solve(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
