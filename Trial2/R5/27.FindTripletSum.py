A = [1, 4, 45, 6, 10, 8] 
s = 22
def triplet_sum():
    A.sort()
    for i in range(len(A)):
        curr_sum = s - A[i]
        low = i+1; high = len(A)-1
        while low < high:
            if A[low] + A[high] == curr_sum:
                return True
            elif A[low] + A[high] < curr_sum:
                low += 1
            else:
                high -= 1

    return False

print(triplet_sum())
