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

def f():
    arr1, arr2 = getInput()
    found_item_at = 0; s = 0; max_len = 0
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            if found_item_at:
                if i < len(arr2) and found_item_at+1< len(arr2[0]) and arr1[i][j] == arr2[i][found_item_at+1]:
                    s += 1
                    found_item_at += 1
                else:
                    max_len = max(max_len, s)
                    s = 0
                    found_item_at = 0
            elif i < len(arr2) and arr1[i][j] in arr2[i]:
                found_item_at = arr2[i].index(arr1[i][j])
                s += 1
    
    print(max_len)


f()