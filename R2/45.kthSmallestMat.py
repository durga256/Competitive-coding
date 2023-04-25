#Kth smallest element in a row-cpumn wise sorted matrix
arr =[[10, 20, 30, 40],[15, 25, 35, 45],[24, 29, 37, 48],[32, 33, 39, 50]]; k = 3

def kth():
    temp = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            temp.append(arr[i][j])

    temp.sort()
    print(temp)
    return temp[k-1]

print(kth())