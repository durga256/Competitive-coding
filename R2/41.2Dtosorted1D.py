mat = [ [10, 20, 30, 40],[15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]

def prin():
    temp = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            temp.append(mat[i][j])

    temp.sort()
    print(temp)

prin()