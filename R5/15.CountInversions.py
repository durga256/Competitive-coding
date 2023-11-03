arr = [12, 11, 13, 5, 6, 7]
arr = [1, 20, 6, 4, 5]

def count_inversions(arr, inversions):
    if len(arr) > 1:
        mid_idx = len(arr)//2

        L = arr[:mid_idx]
        R = arr[mid_idx:]

        inversions += count_inversions(L, inversions)
        inversions += count_inversions(R, inversions)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                inversions += len(L) - i
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1; k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1; k += 1

    return inversions



print(count_inversions(arr, 0))
