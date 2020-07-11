# A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

# A basic queue has the following operations:

# Enqueue: add a new element to the end of the queue.
# Dequeue: remove the element from the front of the queue and return it.
# In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

# 1 x: Enqueue element  into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.
# For example, a series of queries might be as follows:

# image

# Function Description

# Complete the put, pop, and peek methods in the editor below. They must perform the actions as described above.

# Input Format

# The first line contains a single integer, , the number of queries.

# Each of the next  lines contains a single query in the form described in the problem statement above. All queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.

# Constraints

# It is guaranteed that a valid answer always exists for each query of types  and .
# Output Format

# For each query of type , return the value of the element at the front of the fifo queue on a new line.

# Sample Input

# 10
# 1 42
# 2
# 1 14
# 3
# 1 28
# 3
# 1 60
# 1 78
# 2
# 2
# Sample Output

# 14
# 14
# Explanation

# image
class MyQueue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def flip(self,s1,s2):
        while s1:
            s2.append(s1.pop())

    def peek(self):
        if not self.s2:
            self.flip(self.s1,self.s2)
        return self.s2[-1]
        
    def pop(self):
        if not self.s2:
            self.flip(self.s1,self.s2)
        return self.s2.pop()

    def put(self, value):
        self.s1.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

