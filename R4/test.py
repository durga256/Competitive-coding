A = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]


def max_area_histogram(arr):
    stack = []
    res = 0
    for i in range(len(arr)):
        popped_idx = i
        if stack and stack[-1][1] > arr[i]:
            while stack and stack[-1][1] > arr[i]:
                temp = stack.pop()
                popped_idx = temp[0]
                res = max(res,temp[1]*(i-popped_idx)) 
        stack.append([popped_idx, arr[i]])

    while stack:
        temp = stack.pop()
        popped_idx = temp[0]
        res = max(res,temp[1]*(len(arr)-popped_idx)) 

    return res

def f():
    n = len(A)
    m = len(A[0])

    for i in range(1,n):
        for j in range(m):
            if A[i][j] != 0:
                A[i][j] += A[i-1][j]

    for i in range(n):
        temp = max_area_histogram(A[i])
        print(temp)

    print(A)

f()