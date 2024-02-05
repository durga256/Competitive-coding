import sys
from collections import defaultdict
#https://codeforces.com/contest/1921/problem/D
sys.stdin = open('CodeForces/input.txt',  'r')

def get_input():
    t = int(input())
    res =  []
    for _ in range(t):
        input()
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res.append([A,B])
 
    return res
 
def f():
    tc = get_input()
    for A, B in tc:
        n = len(A)
        m = len(B)
        l=[0]*(n+1)
        A.sort()
        B.sort()
        for i in range(n):
            l[i+1]=l[i]+abs(A[i]-B[m-1-i])
        r=[0]*(n+1)
        for i in range(n):
            r[i+1]=r[i]+abs(A[n-i-1]-B[i])
        ans=0
        for i in range(n+1):
            ans=max(ans,l[i]+r[n-i])
        print(A, B, l,r,ans)

 
f()
# 6 4     2 1
# 1 2 3 3 5 7

# 0

# 1 2 3 4 5
# 5 4 3 2 1

# 8          5
# 2 5 7 8 8 10

# 4 1
# 6 9

# 10 8    6 4
# 1 3 6 8 9 10

# 6 5     2
# 1 2 7 7 9

# 10 9 7 6 3
# 2 3 5 9 9

# 3
# 10 