# You are given a square grid with some cells open (.) and some blocked (X). Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell. Given a grid, a start and an end position, determine the number of moves it will take to get to the end position.

# For example, you are given a grid with sides  described as follows:

# ...
# .X.
# ...
# Your starting position  so you start in the top left corner. The ending position is . The path is . It takes  moves to get to the goal.

# Function Description
# Complete the minimumMoves function in the editor. It must print an integer denoting the minimum moves required to get from the starting position to the goal.

# minimumMoves has the following parameter(s):

# grid: an array of strings representing the rows of the grid
# startX: an integer
# startY: an integer
# goalX: an integer
# goalY: an integer
# Input Format

# The first line contains an integer , the size of the array grid.
# Each of the next  lines contains a string of length .
# The last line contains four space-separated integers, 

# Constraints

# Output Format

# Print an integer denoting the minimum number of steps required to move the castle to the goal position.

# Sample Input

# 3
# .X.
# .X.
# ...
# 0 0 0 2
# Sample Output

# 3
# Explanation

# Here is a path that one could follow in order to reach the destination in  steps:

# .
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    def next_steps(grid,point,queue,visited):
        rows,cols = len(grid),len(grid[0])
        cx,cy,cs = point
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = cx,cy
            while True:
                nx,ny = nx+dx,ny+dy
                if (0<=nx<rows and 0<=ny<cols and grid[nx][ny]!="X"):
                    if (nx,ny) not in visited:
                        visited.add((nx,ny))
                        queue.append((nx,ny,cs+1))
                else:
                    break
    d = deque()
    visited = set((startX,startY))
    d.append((startX,startY,0))
    while d:
        cur_p = d.popleft()
        if cur_p[:2]==(goalX,goalY):
            return cur_p[2]
        else:
            next_steps(grid,cur_p,d,visited)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
