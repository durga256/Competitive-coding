from sys import stdin
input=lambda :stdin.readline()[:-1]
#https://codeforces.com/contest/1921/problem/G
#Credits to toam @CodeForces
def solve():
  h,w,k=map(int,input().split())
  s=[input() for i in range(h)]
  if h>w:
    t=[['.']*h for i in range(w)]
    for i in range(h):
      for j in range(w):
        t[j][i]=s[i][j]
    s=t
    h,w=w,h
  
  ans=0
  for tt in range(2):
    res=[[0]*w for i in range(h)]
    for x in range(h):
      for y in range(w):
        if s[x][y]=='#':
          for x0 in range(max(0,x-k),x+1):
            L=y-k+(x-x0)
            res[x0][max(0,L)]+=1
            if y!=w-1:
              res[x0][y+1]-=1
    
    for x in range(h):
      for y in range(w):
        if y!=0:
          res[x][y]+=res[x][y-1]
        ans=max(ans,res[x][y])
    
    s=[s[i][::-1] for i in range(h)]
    res=[[0]*w for i in range(h)]
    for x in range(h):
      for y in range(w):
        if s[x][y]=='#':
          for x0 in range(max(0,x-k),x+1):
            L=y-k+(x-x0)
            res[x0][max(0,L)]+=1
            if y!=w-1:
              res[x0][y+1]-=1
    
    for x in range(h):
      for y in range(w):
        if y!=0:
          res[x][y]+=res[x][y-1]
        ans=max(ans,res[x][y])
    
    if tt==0:
      s=[s[i] for i in range(h-1,-1,-1)]
  
  print(ans)
  
  
for _ in range(int(input())):
  solve()