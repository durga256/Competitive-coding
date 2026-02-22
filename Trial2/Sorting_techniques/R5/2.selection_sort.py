arr = [12, 11, 13, 5, 6]

def sel_sort():
    for i in range(len(arr)):
        min_idx = i; j = i
        while j < len(arr):
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1

        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        print(arr)

sel_sort()

    
