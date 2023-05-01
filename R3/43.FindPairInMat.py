#Find a specific pair in matrix
#https://www.geeksforgeeks.org/find-a-specific-pair-in-matrix/
import sys

mat = [[ 1, 2, -1, -4, -20 ],
       [-8, -3, 4, 2, 1 ],
       [ 3, 8, 6, 1, 3 ],
       [ -4, -1, 1, 7, -6],
       [0, -4, 10, -5, 1 ]]

mat = [[-1,-2,-3],
       [-4,-5,-6],
       [-7,-8,-9]]

mat = [[1,5], [4,2]]

def find():
    maxArr = [[-sys.maxsize - 1 for i in range(len(mat[0]))] for i in range(len(mat))]
    
    n = len(mat)
    maxArr[n-1][n-1] = mat[n-1][n-1]
    maxv = mat[n-1][n-1]
    
    for i in range(n-2,-1,-1):
        if mat[n-1][i] > maxv:
            maxv = mat[n-1][i]
        maxArr[n-1][i] = maxv

    maxv = mat[n-1][n-1]
    for i in range(n-2,-1,-1):
        if mat[i][n-1] > maxv:
            maxv = mat[i][n-1]
        maxArr[i][n-1] = maxv

    maxValue = -sys.maxsize - 1
    for i in range(n-2,-1,-1):
        for j in range(n-2,-1,-1):
            if maxArr[i+1][j+1] - mat[i][j] > maxValue:
                maxValue = maxArr[i+1][j+1] - mat[i][j]

            maxArr[i][j] = max(mat[i][j], max(maxArr[i][j+1], maxArr[i+1][j]))

    for i in maxArr:
        print(i)

    print(maxValue)


find()