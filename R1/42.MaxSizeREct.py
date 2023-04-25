#Maximum size rectangle
A = [[1,1,1,0,1,1,0,0,0,0,0,1,1],[0,1,0,0,0,0,1,1,1,1,1,0,1],[1,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,0,1,0,0,1],[1,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,1,1,1,0,0,0,1,1,0,0,0],[0,0,0,0,1,1,0,1,0,1,1,0,1],[1,0,0,0,0,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,1,1,1,0,1,0,1],[1,1,0,1,0,0,0,0,1,1,1,1,0],[1,0,1,0,0,1,1,0,1,0,0,1,0],[0,0,1,1,0,0,0,0,0,0,1,0,1],[0,0,1,0,1,0,0,0,0,0,1,1,0],[1,0,0,1,0,1,1,0,1,0,0,1,0],[0,1,1,0,0,0,1,1,0,1,1,1,1]]

def maxRect():
    count = 0; temp = []
    for i in range(len(A)):
        count = 0; max_count = 0
        for j in range(len(A[0])):
            if A[i][j] == 1:
                count += 1
            else:
                count = 0
            max_count = max(max_count, count)
        temp.append(max_count)

    #find if 2 or more row rectangles are possible
    max_count = 0; count = 0
    for i in range(len(temp)):
        if temp[i] == len(A[0]):
            count += len(A[0])
        else:
            count = 0
        max_count = max(count, max_count)
    
    print(temp)
    if max_count != 0:
        return max_count
    return max(temp)

print(maxRect())
