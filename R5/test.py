import sys
sys.stdout = open('CodeForces/output.txt', 'w')

import heapq

matrix2 = [[1, 3, 4],
           [2, 5, 6],
           [7, 8, 9]]

class Node:
    def __init__(self, data, r, c) -> None:
        self.data = data
        self.r = r
        self.c = c
    def __lt__(self, other):
        return self.data < other.data
def f(mat):
    minheap = []; n = len(mat); m = len(mat[0])

    for i in range(n):
        temp = Node(mat[i][0], i, 0)
        heapq.heappush(minheap, temp)

    count = 0
    median_count = (n*m)//2
    print(median_count)

    while count <= median_count:
        popped = heapq.heappop(minheap)

        if popped.c+1 < m:
            temp = Node(mat[popped.r][popped.c+1], popped.r, popped.c+1)
            heapq.heappush(minheap, temp)
        print(popped.data, count)
        count += 1
        

    print(popped.data)

f(matrix2)

