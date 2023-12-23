n = "218765"
n = [2,2,7,5,4,3,2,2,1]
arr = [1,2,0,3,0,1,2,4]

def bin_search(arr, l, h, pivot):
    if l <= h:
        mid = (h-l)//2+l

        if (mid == len(arr)-1 or arr[mid+1] <= pivot) and arr[mid] > pivot:
            return mid
        elif arr[mid] > pivot:
            return bin_search(arr, mid+1,h,pivot)
        else:
            return bin_search(arr, l, mid-1, pivot)

def f():
    pivot_idx = -1
    n = len(arr)
    print(arr)
    for i in range(n-1,0,-1):
        if arr[i] > arr[i-1]:
            pivot_idx = i-1
            break

    if pivot_idx == -1:
        arr[:] = reversed(arr[:])
        return arr
    
    min_idx = bin_search(arr,pivot_idx+1, len(arr)-1, arr[pivot_idx])
    print(min_idx)

    arr[min_idx], arr[pivot_idx] = arr[pivot_idx], arr[min_idx]
    arr[pivot_idx+1:] = reversed(arr[pivot_idx+1:])

    return arr

print(f())