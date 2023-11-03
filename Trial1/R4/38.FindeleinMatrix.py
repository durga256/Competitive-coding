#Search an element in a matriix
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 3

l = [3,4,5,13,13,15,15,24,30,31,13,14,19,19,27,31,32,33,35,62,14,23,24,25,36,37,38,44,44,63,30,34,36,38,40,42,43,47,55,65,36,39,40,41,42,51,51,58,59,69,43,44,44,49,56,59,64,64,75,82,46,46,47,63,64,66,67,70,85,89,54,57,58,65,67,70,74,88,88,93,70,72,75,76,90,90,91,93,93,98,84,85,93,95,96,97,97,99,100,100]
n = 10; m= 10; k = 0; x= 63
mat = []
for i in range(n):
    temp = []
    for i in range(m):
        temp.append(l[k])
        k += 1
    mat.append(temp)

def search():
    m = len(matrix); n = len(matrix[0])
    #search in rows. finalize the row it should be in
    low = 0; high = m - 1; row_to_search = 0
    while low < high:
        mid_idx = (high - low)//2 + low
        if matrix[mid_idx][0] == target:
            return True
        elif matrix[mid_idx][0] > target:
            high = mid_idx
        else:
            low = mid_idx
        if high - low <= 1:
            if matrix[low][n-1] > target:
                row_to_search = low
                break
            row_to_search = high
            break
    print(row_to_search)
    low = 0; high = len(matrix[row_to_search]) - 1
    while low < high:
        mid_idx = (high-low)//2+low
        if matrix[row_to_search][mid_idx] == target:
            return True
        elif matrix[row_to_search][mid_idx] > target:
            high = mid_idx - 1
        else:
            low = mid_idx + 1

    return False

print(search())


