from collections import deque 
import sys

sys.stdout = open('CodeForces/output.txt', 'w')

class Solution:
    def shortestDistance(self, maze, start, destination) -> int:
        m, n = len(maze), len(maze[0])
        rs, cs = start
        rd, cd = destination
        dist = [[sys.maxsize-1] * n for _ in range(m)]
        dist[rs][cs] = 0
        q = deque([(rs, cs)])
        while q:
            i, j = q.popleft()
            for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                x, y, step = i, j, dist[i][j]
                while 0 <= x + a < m and 0 <= y + b < n and maze[x + a][y + b] == 0:
                    x, y, step = x + a, y + b, step + 1
                if step < dist[x][y]:
                    dist[x][y] = step
                    q.append((x, y))

        for i in dist:
            print(i)
        return -1 if dist[rd][cd] == sys.maxsize-1 else dist[rd][cd]
    
arr = [[0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0],
       [1, 1, 0, 1, 1],
       [0, 0, 0, 0, 0]]
start = [0,4]
end = [3,2]

sol = Solution()
print(sol.shortestDistance(arr,start,end))
