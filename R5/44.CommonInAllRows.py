mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]

def f():
    d = {}

    for i in range(len(mat[0])):
        d[mat[0][i]] = 0

    for i in range(1,len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] in d and d[mat[i][j]] == i-1:
                d[mat[i][j]] = i

    for i in d:
        if d[i]:
            print(i)

    print(d)

f()