mat = [[10, 20, 30, 40], 
       [15, 25, 35, 45],
       [27, 29, 37, 48], 
       [32, 33, 39, 50]]
x = 29

l = [3,4,5,13,13,15,15,24,30,31,13,14,19,19,27,31,32,33,35,62,14,23,24,25,36,37,38,44,44,63,30,34,36,38,40,42,43,47,55,65,36,39,40,41,42,51,51,58,59,69,43,44,44,49,56,59,64,64,75,82,46,46,47,63,64,66,67,70,85,89,54,57,58,65,67,70,74,88,88,93,70,72,75,76,90,90,91,93,93,98,84,85,93,95,96,97,97,99,100,100]
n = 10; m= 10; k = 0; x= 63
mat = []
for i in range(n):
    temp = []
    for i in range(m):
        temp.append(l[k])
        k += 1
    mat.append(temp)

print(mat)
def search_ele():
    i = 0; j = m-1
    while i < len(mat) and j >= 0:
        if mat[i][j] == x:
            return (i,j)
        if mat[i][j] < x:
            i+= 1
        else:
            j -= 1

print(search_ele())
