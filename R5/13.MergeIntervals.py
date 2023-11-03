arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
arr = [[1,3],[2,4],[6,8],[9,10]]

def MergeIntervals():
    n = len(arr)
    for i in range(1,n):
        key = arr[i]

        j = i-1
        while j >=0 and arr[j][0] > key[0]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
    result = [arr[0]]
    for i in range(1,n):
        if arr[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], arr[i][1])
        else:
            result.append(arr[i])

    print(result)

MergeIntervals()