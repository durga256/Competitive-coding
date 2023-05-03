arr = [2,3,7,8,10]
c = 11
def sub(arr, n, c):
    if n == 0:
        return False
    if c == 0:
        return True
    return sub(arr,n-1,c-arr[n-1]) or sub(arr, n-1, c)

print(sub(arr,len(arr),c))