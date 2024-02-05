import sys
#https://codeforces.com/contest/1921/problem/F
sys.stdin = open('CodeForces/input.txt',  'r')

def get_input():
    t = int(input())
    res =  []
    for _ in range(t):
       n, q = list(map(int, input().split()))
       temp = []
       temp.append(list(map(int, input().split())))
       for i in range(q):
           temp.append(list(map(int, input().split())))
       res.append(temp)

    return res    

def f():
    tc = get_input()
    for i in tc:
        arr = i[0]
        queries = i[1:]
        for s,d,k in queries:
            s -= 1
            res = 0
            temp_k = 1
            temp_d = 0
            while temp_k <= k and s+temp_d < len(arr):
                res += temp_k*arr[s+temp_d]
                temp_d += d
                temp_k += 1
            print(res,end=" ")
        print()


f()
#Below code Credits to toam @CodeForces
from sys import stdin
input=lambda :stdin.readline()[:-1]

def solve():
  n,q=map(int,input().split())
  a=list(map(int,input().split()))
  B=int((n+0.1)**0.5)
  query=[[] for i in range(B+1)]
  ans=[0]*q
  for i in range(q):
    s,d,k=map(int,input().split())
    s-=1
    if d>B:
      t=0
      for j in range(k):
        t+=(j+1)*a[s+(d*j)]
      ans[i]=t
    else:
      query[d].append([s,k,i])
  
  for d in range(1,B+1):
    if len(query[d])==0:
      continue
    cum=[0]*(n+d)
    cum2=[0]*(n+d)
    for i in range(n):
      cum[i+d]=cum[i]+a[i]
      cum2[i+d]=cum2[i]+a[i]*(i//d+1)
    for s,k,i in query[d]:
      res=cum2[s+d*k]-cum2[s]
      res-=(cum[s+d*k]-cum[s])*(s//d)
      ans[i]=res
  print(*ans)

for _ in range(int(input())):
  solve()