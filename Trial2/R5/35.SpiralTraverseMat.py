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

#Another solution using travelling a matrix in all 4 directions concept
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        ret = []
        i = j = 0
        l, r, lo, up = (0, -1), (0, 1), (1, 0), (-1, 0)
        d = r
        left, right, lower, upper = -1, m, n, -1
        while True:
            if d == r and j == right \
                or d == lo and i == lower \
                or d == l and j == left \
                or d == up and i == upper:
                    return ret
            ret.append(matrix[i][j])
            i += d[0]
            j += d[1]
            if d == r and j == right:
                i -= d[0]
                j -= d[1]
                d = lo
                i += d[0]
                j += d[1]
                upper += 1
            elif d == lo and i == lower:
                i -= d[0]
                j -= d[1]
                d = l
                i += d[0]
                j += d[1]
                right -= 1
            elif d == l and j == left:
                i -= d[0]
                j -= d[1]
                d = up
                i += d[0]
                j += d[1]
                lower -= 1
            elif d == up and i == upper:
                i -= d[0]
                j -= d[1]
                d = r
                i += d[0]
                j += d[1]
                left += 1
