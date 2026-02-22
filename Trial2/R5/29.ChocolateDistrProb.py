arr = [3, 4, 1, 9, 56, 7, 9, 12] ; m = 5

def choc():
    arr.sort()
    low = 0; high = m-1
    res = arr[high] - arr[low]
    while high < len(arr):
        res = min(res, arr[high] - arr[low])
        low += 1; high += 1

    print(res)

choc()
