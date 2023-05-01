#Common elements in all rows of a given matrix

mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]

def common():
    d = {}; n = len(mat[0])
    for i in range(len(mat)):
        for j in range(n):
            if mat[i][j] not in d.keys():
                d[mat[i][j]] = set()
                d[mat[i][j]].add(i)
            else:
                d[mat[i][j]].add(i)

    print(d)

    for i in d.keys():
        if len(d[i]) == n-1:
            print(i)



common()