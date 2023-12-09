#Rotate matrix by 90 degrees anticlockwise
arr = [[1,2,3,4, 21],
       [5,6,7,8, 22],
       [9,10,11,12, 23],
       [13,14,15,16, 24],
       [25,26,27,28,29]]

#[13,9,5,1]
#[14,10,6,2]
#[15,11,7,3]
#[16,12,8,4]
def f():
    temp = []
    for i in range(len(arr)):
        temp.append([-1]*len(arr[0]))
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            temp[j][i] = arr[i][len(arr)-j-1]

    print(temp)

#f()

#Rotate matrix clockwise w/o extra space

def f2():
    n = len(arr); m = len(arr[0])
    for j in range(n//2):
        for i in range(n-1-(2*j)):
            a = arr[n-i-1-j][j]
            b = arr[j][i+j]
            c = arr[i+j][m-j-1]
            d = arr[n-1-j][m-i-1-j]
            arr[j][i+j] = a
            arr[i+j][m-j-1] = b
            arr[n-1-j][m-i-1-j] = c
            arr[n-i-1-j][j] = d

    print(arr)

f2()