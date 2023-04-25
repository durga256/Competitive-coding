import sys
arr = [7, 3, 2, 4, 9, 12, 56]; m = 3 

def chocolateDistr():
    arr.sort()
    min_diff = sys.maxsize
    for i in range(len(arr)-m+1):
        min_diff = min(min_diff, arr[i+m-1]-arr[i])

    print(min_diff)

chocolateDistr()
