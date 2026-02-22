s = "aaaa"

def f(s,i,j):
    if i == j:
        return 1
    
    if i > j:
        return 0
    
    if s[i] == s[j]:
        return 1+f(s,i+1,j)+f(s,i,j-1)
    else:
        return f(s,i+1,j)+f(s,i,j-1)-f(s,i+1,j-1)
    
print(f(s,0,len(s)-1))