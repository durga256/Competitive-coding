S1 = 'AGGTAB'; S2 = 'GXTXAYB'

def f(s1,s2,n,m):
    if n == 0 or m == 0:
        return 0
    
    if s1[n-1] == s2[m-1]:
        return 1+f(s1,s2,n-1,m-1)
    else:
        return max(f(s1,s2,n-1,m),f(s1,s2,n,m-1))
    
print(f(S1, S2, len(S1), len(S2)))

