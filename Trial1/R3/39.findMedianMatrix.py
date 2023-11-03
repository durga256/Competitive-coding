#Find median in a row wise sorted matrix

matrix = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]

def findMed():
    temp = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp.append(matrix[i][j])
    temp.sort()
    return temp[len(temp)//2]


print(findMed())
        