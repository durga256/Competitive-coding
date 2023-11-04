import heapq
mat = [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [24, 29, 37, 48],
        [32, 33, 39, 50]]
k = 3
class Node:
    def __init__(self, data, row, col) -> None:
        self.data = data
        self.row = row
        self.col = col
    def __lt__(self, other):
        return self.data < other.data

def kthSmall():
    minheap = []; n = len(mat); m = len(mat[0]); count = 0

    for i in range(n):
        temp = Node(mat[i][0], i, 0)
        heapq.heappush(minheap, temp)


    while count < k:
        temp = heapq.heappop(minheap)
        count += 1

        if temp.col+1 < m:
            temp_node = Node(mat[temp.row][temp.col+1], temp.row, temp.col+1)
            heapq.heappush(minheap, temp_node)

    print(temp.data)

kthSmall() 


