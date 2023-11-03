import sys

arr = [40,20,30,10,30]
ans = sys.maxsize
temp = 0

def mcm(i,j):
    global ans, temp
    if i >= j:
        return 0
    for k in range(i,j):
        temp = mcm(i,k)+mcm(k+1,j) + arr[i-1]*arr[k]*arr[j]
        print(temp, i, j)
        ans = min(ans, temp)
    return ans

print(mcm(1,len(arr)-1))
