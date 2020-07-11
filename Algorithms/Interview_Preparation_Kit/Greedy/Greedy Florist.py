# A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers and the money he makes. To do this, he decides he'll multiply the price of each flower by the number of that customer's previously purchased flowers plus . The first flower will be original price, , the next will be  and so on.

# Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers, determine the minimum cost to purchase all of the flowers.

# For example, if there are  friends that want to buy  flowers that cost  each will buy one of the flowers priced  at the original price. Having each purchased  flower, the first flower in the list, , will now cost . The total cost will be .

# Function Description

# Complete the getMinimumCost function in the editor below. It should return the minimum cost to purchase all of the flowers.

# getMinimumCost has the following parameter(s):

# c: an array of integers representing the original price of each flower
# k: an integer, the number of friends
# Input Format

# The first line contains two space-separated integers  and , the number of flowers and the number of friends.
# The second line contains  space-separated positive integers , the original price of each flower.

# Constraints

# Output Format

# Print the minimum cost to buy all  flowers.

# Sample Input 0

# 3 3
# 2 5 6
# Sample Output 0

# 13
# Explanation 0

# There are  flowers with costs  and  people in the group. If each person buys one flower, the total cost of prices paid is  dollars. Thus, we print  as our answer.

# Sample Input 1

# 3 2
# 2 5 6
# Sample Output 1

# 15
# Explanation 1

# There are  flowers with costs  and  people in the group. We can minimize the total purchase cost like so:

# The first person purchases  flowers in order of decreasing price; this means they buy the more expensive flower () first at price  dollars and the less expensive flower () second at price  dollars.
# The second person buys the most expensive flower at price  dollars.
# We then print the sum of these purchases, which is , as our answer.

# Sample Input 2

# 5 3
# 1 3 5 7 9
# Sample Output 2

# 29
# Explanation 2

# The friends buy flowers for ,  and ,  and  for a cost of .
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort()
    if k>=len(c):
        return sum(c)
    ans = 0
    ind = len(c)
    it = 0
    while ind>=0:
        it+=1
        for _ in range(k):
            ind-=1
            if ind>=0:
                ans+=it*c[ind]
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
