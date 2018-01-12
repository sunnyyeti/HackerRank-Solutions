#!/bin/python

import sys

def climbingLeaderboard(scores, alice):
    # Complete this function
    uniques =[]
    pre = -1
    for s in scores:
        if s!=pre:
            uniques.append(s)
            pre = s
    pre = len(uniques)
    ranks = []
    for a in alice:
        flag = False
        for i in xrange(pre,0,-1):
            if a<uniques[i-1]:
                ranks.append(i+1)
                pre = i
                flag = True
                break
            if a == uniques[i-1]:
                ranks.append(i)
                pre = i-1
                flag = True
                break
        if not flag:
            ranks.append(1)
            pre = 0
    return ranks
           
                
    
      
if __name__ == "__main__":
    n = int(raw_input().strip())
    scores = map(int, raw_input().strip().split(' '))
    m = int(raw_input().strip())
    alice = map(int, raw_input().strip().split(' '))
    result = climbingLeaderboard(scores, alice)
    print "\n".join(map(str, result))