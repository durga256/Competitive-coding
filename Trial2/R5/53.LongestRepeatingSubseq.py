s1 = "axxxy"

def f(s1, n, m):
    if n==0 or m==0:
        return 0
    
    if s1[n-1] == s1[m-1] and n != m :
        return 1+f(s1,n-1,m-1)
    else:
        return max(f(s1,n-1,m),f(s1,n,m-1))
    
print(f(s1,len(s1),len(s1)))
