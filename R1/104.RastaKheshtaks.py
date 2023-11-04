import sys
sys.stdin = open('CodeForces/input.txt', 'r')
sys.stdout = open('CodeForces/output.txt', 'w')

def getInput():
    N , M = input().split()
    arr = []
    for i in range(int(N)):
        temp = [int(x) for x in input().split()]
        arr.append(temp)
    X, Y = input().split()
    arr2 = []
    for i in range(int(X)):
        temp = [int(x) for x in input().split()]
        arr2.append(temp)
 
    return (arr, arr2)
 
def find_hash(arr, col1, col2, row):
    if col1 >= len(arr[0]) or col2 >= len(arr[0]) or col1 == col2:
        return 0
    hashCol = []
    add = 0
    radix = 256
    end_row = row+(col2-col1)
    
    if end_row >= len(arr):
        return 0
    
    for i in range(col1, col2+1):
        for j in range(row, end_row+1):
            add = add + (radix**(row-j-1) *
                         arr[j][i])% 101
        hashCol.append(add % 101)
        add = 0
    return hashCol
 
def f():
    arr1, arr2 = getInput()
    dp1 = []; dp2 = []
    # for i in range(len(arr1[0])+1):
    #     temp = []
    #     for j in range(len(arr1[0])+1):
    #         temp.append([])
    #     dp1.append(temp)
    # for i in range(len(arr2[0])+1):
    #     temp = []
    #     for j in range(len(arr2[0])+1):
    #         temp.append([])
    #     dp2.append(temp)
 
    for i in range(len(arr1)):
        j = 0
        while j < len(arr1[0]):
            for k in range(j,len(arr1[0])):
                temp = find_hash(arr1, j, k, i)
                if temp != 0 and len(temp) > 1:
                    dp1.append(temp)
            j += 1
 
    # for i in range(len(dp1)):
    #     print(dp1[i])
 
    dp1.sort()
 
    for i in range(len(arr2)):
        j = 0
        while j < len(arr2[0]):
            for k in range(j,len(arr2[0])):
                temp = find_hash(arr2, j, k, i)
                if temp != 0 and len(temp) > 1:
                    dp2.append(temp)
            j += 1
 
    dp2.sort()
    # for i in range(len(dp2)):
    #     print(dp2[i])
 
    i = 0; j = 0; res = 0; flag = True
    while i < len(dp1) and j < len(dp2):
        if dp1[i][0] == dp2[j][0] and len(dp1[i]) == len(dp2[j]):
            # for k in range(len(dp1[i])):
            #     if dp1[i][k] != dp2[j][k]:
            #         flag = False
            #         if dp1[i][k] < dp2[j][k]:
            #             i += 1
            #         else:
            #             j += 1
            #         break
            # if flag:
                res = max(res, len(dp1[i]))
                i += 1; j += 1            
        elif dp1[i][0] < dp2[j][0]:
            i += 1
        else:
            j += 1
 
    print(res)
 
f()