#Rotate matrix by 90 degrees anticlockwise
arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

def rot():
    n=len(arr); m = len(arr[0])
    temp = [[0 for i in range(m)]for i in range(m)]

    for i in range(n):
        for j in range(m):
            temp[j][i] = arr[i][n-1-j]

    print(temp)

rot()
