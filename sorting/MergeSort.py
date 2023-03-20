arr_og = [12,11,13,5,6,7]
ans = 0
def merge_sort(arr):
    global ans
    k = 0
    if len(arr) > 1:
        mid_idx = len(arr)//2

        L = merge_sort(arr[:mid_idx])
        R = merge_sort(arr[mid_idx:])
        i = 0; j = 0
        while i < len(L) and j < len(R):
            if R[j] < L[i]:
                print(R[j], L[i])
                arr[k] = R[j]
                k += 1; j += 1; ans += mid_idx-i
            else:
                arr[k] = L[i]
                k += 1; i += 1
        while i < len(L):
            arr[k] = L[i]
            k += 1; i += 1
        while j < len(R):
            arr[k] = R[j]
            k += 1; j += 1
        return arr
    else:
        return arr

print(merge_sort(arr_og))
print(ans)