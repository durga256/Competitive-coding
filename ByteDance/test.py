from collections import deque
import sys

arr = [[0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0],
       [1, 1, 0, 1, 1],
       [0, 0, 0, 0, 0]]
start = [0,4]
end = [3,2  ]

def f():
    m,n = len(arr), len(arr[0])
    dist = [[sys.maxsize]*n for i in range(m)]
    rs, cs = start
    dist[rs][cs] = 0
    rd,cd = end
    q = deque([(rs,cs)])
    while q:
        i,j = q.popleft()
        for a,b in [[0,-1],[0,1],[1,0],[-1,0]]:
            x, y, step = i,j,dist[i][j]
            while 0<= x+a < m and 0<= y+b < n and arr[x+a][y+b] == 0:
                x,y,step = x+a,y+b, step+1
            if step < dist[x][y]:
                dist[x][y] = step
                q.append([x,y])
        
    return -1 if dist[rd][cd] == sys.maxsize else dist[rd][cd]

print(f())