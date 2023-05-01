#Rotate matrix by 90 degrees

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def rot():
    temp = [[0 for i in range(len(arr[0]))]for j in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            temp[j][i] = arr[i][len(arr)-1-j]
        
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = temp[i][j]

rot()