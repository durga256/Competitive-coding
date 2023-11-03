#Find row with maximum no. of 1's
mat = [[0, 0, 0, 1],[0, 1, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]

def coun():
    max_sofar = 0; max_sofar_idx = -1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if len(mat[0]) - j < max_sofar:
                break
            if mat[i][j] == 1:
                max_sofar = max(max_sofar, len(mat[0])-j)
                max_sofar_idx = i
                break
    print(max_sofar)
    return max_sofar_idx

print(coun())