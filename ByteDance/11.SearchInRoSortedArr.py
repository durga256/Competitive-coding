arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]; key = 11

def bin_search(arr,l,h,key):
    if l <= h:
        mid = (h-l)//2+l

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return bin_search(arr, mid+1,h,key)
        else:
            return bin_search(arr,l,mid-1,key)
    return -1


def find_pivot(arr,l,h):
    if l <= h:
        mid = (h-l)//2+l

        if mid < h and arr[mid+1] < arr[mid]:
            return mid
        elif mid > l and arr[mid-1] > arr[mid]:
            return mid-1
        if arr[l] < arr[mid]:
            return find_pivot(arr,mid+1,h)
        return find_pivot(arr, l,mid-1)
    return -1
def f():
    #find pivot
    pivot_idx = find_pivot(arr,0,len(arr)-1)

    if key < arr[0]:
        return bin_search(arr, pivot_idx+1,len(arr)-1,key)
    return bin_search(arr, 0, pivot_idx, key)

print(f())