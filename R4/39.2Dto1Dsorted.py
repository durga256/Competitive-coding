mat = [
[10, 20, 30, 40],
[15, 25, 35, 45],
[27, 29, 37, 48],
[32, 33, 39, 50]
]

import heapq

class Node:
    def __init__(self, data, row, col) -> None:
        self.data = data
        self.row = row
        self.col = col
    def __lt__(self, other):
        return self.data < other.data

def sor():
    minheap = []; n = len(mat); m = len(mat[0])
    matrix = []
    for i in range(n):
        matrix.append([0]*m)

    for i in range(n):
        temp = Node(mat[i][0], i, 0)
        heapq.heappush(minheap, temp)

    i = j = 0

    while minheap:
        temp = heapq.heappop(minheap)
        data = temp.data
        row = temp.row
        col = temp.col
        matrix[i][j] = data
        if j == m-1:
            i += 1; j = 0
        else:
            j += 1
        print(data, end=" ")

        if col + 1 < m:
            col += 1
            temp_node = Node(mat[row][col], row, col)
            heapq.heappush(minheap, temp_node)
    print(matrix)

sor()