# A  Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid. Cells are marked either + or -. Cells marked with a - are to be filled with the word list.

# The following shows an example crossword from the input  grid and the list of words to fit, :

# Input 	   		Output

# ++++++++++ 		++++++++++
# +------+++ 		+POLAND+++
# +++-++++++ 		+++H++++++
# +++-++++++ 		+++A++++++
# +++-----++ 		+++SPAIN++
# +++-++-+++ 		+++A++N+++
# ++++++-+++ 		++++++D+++
# ++++++-+++ 		++++++I+++
# ++++++-+++ 		++++++A+++
# ++++++++++ 		++++++++++
# POLAND;LHASA;SPAIN;INDIA
# Function Description

# Complete the crosswordPuzzle function in the editor below. It should return an array of strings, each representing a row of the finished puzzle.

# crosswordPuzzle has the following parameter(s):

# crossword: an array of  strings of length  representing the empty grid
# words: a string consisting of semicolon delimited strings to fit into 
# Input Format

# Each of the first  lines represents , each of which has  characters, .

# The last line contains a string consisting of semicolon delimited  to fit.

# Constraints




# Output Format

# Position the words appropriately in the  grid, then return your array of strings for printing.

# Sample Input 0

# +-++++++++
# +-++++++++
# +-++++++++
# +-----++++
# +-+++-++++
# +-+++-++++
# +++++-++++
# ++------++
# +++++-++++
# +++++-++++
# LONDON;DELHI;ICELAND;ANKARA
# Sample Output 0

# +L++++++++
# +O++++++++
# +N++++++++
# +DELHI++++
# +O+++C++++
# +N+++E++++
# +++++L++++
# ++ANKARA++
# +++++N++++
# +++++D++++
# Sample Input 1

# +-++++++++
# +-++++++++
# +-------++
# +-++++++++
# +-++++++++
# +------+++
# +-+++-++++
# +++++-++++
# +++++-++++
# ++++++++++
# AGRA;NORWAY;ENGLAND;GWALIOR
# Sample Output 1

# +E++++++++
# +N++++++++
# +GWALIOR++
# +L++++++++
# +A++++++++
# +NORWAY+++
# +D+++G++++
# +++++R++++
# +++++A++++
# ++++++++++
# Sample Input 2

# XXXXXX-XXX
# XX------XX
# XXXXXX-XXX
# XXXXXX-XXX
# XXX------X
# XXXXXX-X-X
# XXXXXX-X-X
# XXXXXXXX-X
# XXXXXXXX-X
# XXXXXXXX-X
# ICELAND;MEXICO;PANAMA;ALMATY
# Sample Output 2

# XXXXXXIXXX
# XXMEXICOXX
# XXXXXXEXXX
# XXXXXXLXXX
# XXXPANAMAX
# XXXXXXNXLX
# XXXXXXDXMX
# XXXXXXXXAX
# XXXXXXXXTX
# XXXXXXXXYX
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
def get_possible_starts(crossword):
    ans = []
    for i in range(10):
        for j in range(10):
            if crossword[i][j]=="-":
                if (j==0 or crossword[i][j-1]!="-") and (j<9 and crossword[i][j+1]=="-"):
                    length = 1
                    nj = j+1
                    while nj<10 and crossword[i][nj]=="-":
                        length+=1
                        nj+=1
                    ans.append((i,j,'h',length))
                elif (i==0 or crossword[i-1][j]!="-") and (i<9 and crossword[i+1][j]=='-'):
                    length = 1
                    ni = i+1
                    while ni<10 and crossword[ni][j]=="-":
                        length+=1
                        ni+=1
                    ans.append((i,j,'v',length))
    return ans
def crosswordPuzzle(crossword, words):
    crossword = list(map(lambda x:list(x),crossword))
    words = words.split(";")
    # words_len = {}
    # for w in words:
    #     words_len.setdefault(len(w),[]).append(w)
    pos = get_possible_starts(crossword)
    used = set()
    def issuccess(pos_ind):
        if pos_ind==len(pos):
            return True
        i,j,d,l = pos[pos_ind]
        for wind,w in enumerate(words):
            if len(w)==l and wind not in used:
                if d=="h":
                    for dj,c in enumerate(w):
                        if crossword[i][j+dj] not in ["-",c]:
                            break #预先判断能不能放进去
                    else:#能的就 放进去 ，然后把旧的保存起来
                        old_w = "".join(crossword[i][j:j+l])
                        crossword[i][j:j+l] = w
                        used.add(wind)
                        if issuccess(pos_ind+1):
                            return True
                        else:
                            crossword[i][j:j+l] = old_w
                            used.remove(wind)
                else:
                    for di,c in enumerate(w):
                        if crossword[i+di][j] not in ["-",c]:
                            break
                    else:
                        old_w = "".join(crossword[i+di][j] for di in range(l))
                        for di,c in enumerate(w):
                            crossword[i+di][j]=c
                        used.add(wind)
                        if issuccess(pos_ind+1):
                            return True
                        else:
                            for di,c in enumerate(old_w):
                                crossword[i+di][j]=c
                            used.remove(wind)
    issuccess(0)
    return list(map(lambda x:"".join(x),crossword))

                

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
