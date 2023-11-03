import sys

s = "pitin"

def isPal(s,i,j):
    flag = True
    while i < j:
        if s[i] != s[j]:
            flag = False
            break
        i += 1; j-= 1
    return flag

def palPart(s,i,j):
    ans = sys.maxsize
    if i>= j:
        return 0
    if isPal(s,i,j):
        return 0
    for k in range(i,j):
        temp = palPart(s,i,k) + palPart(s,k+1,j) + 1
        ans = min(ans,temp)
    return ans

print(palPart(s,0,len(s)-1))
