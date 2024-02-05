#https://codeforces.com/contest/1921/problem/E
#Credits to toam @CodeForces
from sys import stdin
input=lambda :stdin.readline()[:-1]
 
def solve():
  h,w,xa,ya,xb,yb=map(int,input().split())
  if xa<=xb:
    if (xa-xb)%2==1:
      d=(xb-xa)//2
      La=max(1,ya-d-1)
      Ra=min(w,ya+d+1)
      Lb=max(1,yb-d)
      Rb=min(w,yb+d)
      if La<=Lb<=Rb<=Ra:
        print('Alice')
      else:
        print('Draw')
    else:
      d=(xb-xa)//2
      ans='Bob'
      for dy in range(-1,2):
        if 1<=ya+dy<=w:
          La=max(1,ya+dy-d+1)
          Ra=min(w,ya+dy+d-1)
          Lb=max(1,yb-d)
          Rb=min(w,yb+d)
          if Lb<=La<=Ra<=Rb:
            pass
          else:
            ans='Draw'
      print(ans)
  else:
    print('Draw')
 
 
for _ in range(int(input())):
  solve()