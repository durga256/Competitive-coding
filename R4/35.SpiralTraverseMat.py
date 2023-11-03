matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def trav():
    top = 0; bottom = len(matrix); left = 0; right = len(matrix[0])
    while top < bottom and left < right:
        for i in range(left, right):
            print(matrix[top][i], end=" ")
        top += 1

        for i in range(top, bottom):
            print(matrix[i][right-1], end=" ")
        right -= 1

        if top < bottom:
            for i in range(right-1,left-1,-1):
                print(matrix[bottom-1][i], end=" ")
            bottom -= 1

        if left < right:
            for i in range(bottom-1,top-1,-1):
                print(matrix[i][left],end=" ")
            left += 1

trav()
