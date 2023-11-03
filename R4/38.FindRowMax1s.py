mat = [[0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       [0, 0, 0, 0]]

#O(n^2)
def findMaxRow():
    left_col_with1 = 0

    n = len(mat); m = len(mat[0])

    while left_col_with1 < m:
        for i in range(n):
            if mat[i][left_col_with1] == 1:
                return i+1
        left_col_with1 += 1

    return -1

#print(findMaxRow())

def bin_search(arr, low, high):
    if low > high:
        return -1
    
    mid = (high-low)//2+low
    if (mid ==0 or arr[mid-1]==0) and arr[mid] == 1:
        return mid
    if arr[mid] == 0:
        return bin_search(arr, mid+1, high)
    else:
        return bin_search(arr, low, mid-1)
    
def findMaxRow():
    n = len(mat); m = len(mat[0]); res = 0; row_idx = 0
    for i in range(n):
        temp = bin_search(mat[i], 0, m-1)
        if temp!= -1 and res < m-1-temp:
            res = m-1-temp
            row_idx = i

    print(row_idx)

findMaxRow()



