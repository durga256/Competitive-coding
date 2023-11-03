mat = [[0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 0, 0]]


def f(arr, low, high):
    if low > high: return -1
    mid = (high-low)//2+low

    if (mid ==0 or arr[mid-1] == 0) and arr[mid] == 1:
        return mid
    if arr[mid] == 0:
        return f(arr,mid+1, high)
    else:
        return f(arr,low,mid-1)
    
        
def f2():
    max_len = 0
    m = len(mat[0])
    for i in range(len(mat)):
        temp = f(mat[i],0,m-1)
        if temp != -1:
            max_len = max(max_len, m-temp)

    print(max_len)

f2()