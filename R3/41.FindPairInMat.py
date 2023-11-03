import sys
mat = [[ 1, 2, -1, -4, -20 ],
       [ -8, -3, 4, 2, 1 ],
       [ 3, 8, 6, 1, 3 ],
       [ -4, -1, 1, 7, -6 ],
       [ 0, -4, 10, -5, 1 ]]

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

mat = [[2,4,-6],
       [12,-44,11],
       [4,33,-1]]

def find():
    n = len(mat); m = len(mat[0])
    temp_arr = [[-sys.maxsize+1 for i in range(m)]for i in range(n)]
    maxv = mat[n-1][m-1]
    temp_arr[n-1][m-1] = maxv

    for i in range(n-2,-1,-1):
        maxv = max(maxv, mat[i][m-1])
        temp_arr[i][m-1] = maxv
    
    maxv = mat[n-1][m-1]
    for i in range(m-2,-1,-1):
        maxv = max(maxv, mat[n-1][i])
        temp_arr[n-1][i] = maxv

    maxv = -sys.maxsize
    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            maxv = max(maxv, temp_arr[i+1][j+1]-mat[i][j])
            temp_arr[i][j] = max(mat[i][j], max(temp_arr[i][j+1], temp_arr[i+1][j]))

    print(temp_arr)
    print(maxv)

find()