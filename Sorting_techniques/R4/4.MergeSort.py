arr = [12, 11, 13, 5, 6, 7]

def MergeSort(arr):
    if len(arr) > 1:
        mid_idx = len(arr)//2

        L = arr[:mid_idx]
        R = arr[mid_idx:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1; k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1; k += 1

MergeSort(arr)
print(arr)
