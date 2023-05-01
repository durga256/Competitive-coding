#Search an element in a matriix
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 3

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


