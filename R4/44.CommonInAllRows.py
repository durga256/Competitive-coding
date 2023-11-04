mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]


def find():
    d = {}
    for i in range(len(mat)):
        for j in mat[i]:
            if j in d:
                d[j].append(i)
            else:
                d[j] = []
                d[j].append(i)

    print(d); 
    res = []
    for i in d:
        if len(set(d[i])) == len(mat):
            res.append(i)

    print(res)


find()