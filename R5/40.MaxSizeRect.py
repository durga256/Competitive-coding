A = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]

def max_rect():
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i != 0 and A[i][j] != 0:
                A[i][j] += A[i-1][j]

    res = 0
    for i in range(len(A)):
        print(find(A[i]))
        res = max(res, find(A[i]))
    print(res)



def find(arr):
    stack = [[0, arr[0]]]; ans = 0; n = len(arr)
    for i in range(len(arr)):
        popped_idx = i
        while stack and stack[-1][1] > arr[i]:
            ans = max(ans, stack[-1][1]*(i-stack[-1][0]))
            popped_idx = stack[-1][0]
            stack.pop()
        stack.append([popped_idx, arr[i]])

    while stack:
        ans = max(ans, stack[-1][1]*(n-stack[-1][0]))
        stack.pop()

    #print(ans)
    return ans

max_rect()
#print(find([6, 2, 5, 4, 5, 1, 6]))

