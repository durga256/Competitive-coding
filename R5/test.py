arr = [12, 11, 13, 5, 6, 7]
arr = [1, 20, 6, 4, 5]

def count(arr, count_inversion):
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        count_inversion += count(L, count_inversion)
        count_inversion += count(R, count_inversion)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                count_inversion += len(L) - i
                arr[k] = R[j]
                j+=1
            k += 1
    return count_inversion

print(count(arr, 0))