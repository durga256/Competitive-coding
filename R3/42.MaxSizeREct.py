#Maximum size rectangle
matrix = [["0", "1"], ["1", "0"]]

def maxRect():
    k = 0; res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i != 0 and int(matrix[i][j]) != 0:
                matrix[i][j] = int(matrix[i][j]) + int(matrix[i-1][j])
            else:
                matrix[i][j] = int(matrix[i][j])

    maxArea = 0
    print(matrix)
    for i in range(len(matrix)):
        maxArea = max(maxArea, find(matrix[i]))

    return maxArea

def find(n):
    stack = [[0, n[0]]]; maxArea = 0
    for i in range(len(n)):
        if n[i] < stack[-1][1]:
            while stack and stack[-1][1] > n[i]:
                maxArea = max(maxArea, stack[-1][1]*(i-stack[-1][0]))
                popped_idx = stack[-1][0]
                stack.pop()
            stack.append([popped_idx, n[i]])
        else:
            stack.append([i, n[i]])

    length_arr = len(n)

    for i in range(len(stack)):
        maxArea = max(maxArea, stack[i][1]*(length_arr - stack[i][0]))

    print(maxArea)
    return maxArea



print(maxRect())


        
