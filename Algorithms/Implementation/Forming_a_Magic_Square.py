#!/bin/python

import sys
import copy
ORIG = [[4,9,2],[3,5,7],[8,1,6]]
def flip_v(ss):
    s = copy.deepcopy(ss)
    for i in xrange(3):
        s[i][0],s[i][2] = s[i][2],s[i][0]
    return s
    
def rotate_clockwise_90(ss):
    s = copy.deepcopy(ss)
    for i in xrange(3):
        for j in xrange(3):
            s[i][j] = ss[2-j][i]
    return s
    
all_squares = [ORIG]
all_squares.append(flip_v(ORIG))
tmp_ = ORIG
for i in xrange(3):
    tmp_ = rotate_clockwise_90(tmp_)
    all_squares.append(tmp_)
    all_squares.append(flip_v(tmp_))
    
def diff(s1,s2):
    tmp_ = 0
    for i in xrange(3):
        for j in xrange(3):
            tmp_ += abs(s1[i][j]-s2[i][j])
    return tmp_

def formingMagicSquare(s):
    min_dif = 100
    # Complete this function
    for s_ in all_squares:
        if diff(s_,s)<min_dif:
            min_dif = diff(s_,s)
    return min_dif

if __name__ == "__main__":
    s = []
    for s_i in xrange(3):
        s_temp = map(int,raw_input().strip().split(' '))
        s.append(s_temp)
    result = formingMagicSquare(s)
    print result
