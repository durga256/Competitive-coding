#Find median in a row wise sorted matrix

matrix = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]

import heapq

class Node:
    def __init__(self, data: int, row: int, col: int) -> None:
        self.data = data
        self.row = row
        self.col = col
    def __lt__(self, other):
        return self.data < other.data
    
def heap_search():
    minheap = []

    for i in range(len(matrix)):
        temp = Node(matrix[i][0], i, 0)
        heapq.heappush(minheap, temp)

    count = 0; median_index = (len(matrix)*len(matrix[0]))//2

    while count <= median_index:
        temp = heapq.heappop(minheap)

        row = temp.row
        col = temp.col
        data = temp.data

        count += 1

        if col + 1 < len(matrix[0]):
            col += 1
            temp_node = Node(matrix[row][col], row, col)
            heapq.heappush(minheap, temp_node)

    print(temp.data)

heap_search()
    
