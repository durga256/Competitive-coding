arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]; key = 3

def f():
    def binary_pivot(arr):
        l = 0; h = len(arr) - 1
        while l <= h:
            mid = (l+h)//2
            if mid > 0 and arr[mid-1] > arr[mid]:
                return mid
            elif mid < len(arr)-1 and arr[mid+1] < arr[mid]:
                return mid+1
            elif arr[mid] > arr[l]:
                l = mid+1
            else:
                h = mid-1

        return -1
    def bin_search(arr, l, h, key):
        while l <= h:
            mid = (l+h)//2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                l = mid+1
            else:
                h = mid-1
        return -1
    pivot_idx = binary_pivot(arr)
    if pivot_idx != -1:
        if key >= arr[0]:
            return bin_search(arr, 0, pivot_idx-1, key)
        else:
            return bin_search(arr, pivot_idx, len(arr)-1, key)
    else:
        return bin_search(arr, 0, len(arr)-1, key)


    

print(f())