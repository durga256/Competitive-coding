arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]; key = 3

def bin_search(arr,low,high,key):
    if low <= high:
        mid = (high-low)//2+low

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return bin_search(arr,mid+1,high,key)
        else:
            return bin_search(arr,low,mid-1,key)
        
    return -1

def findPivot(self,arr,l,h):
    if l <= h:
        mid = (l+h)//2

        if mid < h and arr[mid] > arr[mid+1]:
            return mid
        if mid > l and arr[mid] < arr[mid-1]:
            return mid-1
        if arr[l] >= arr[mid]:
            return findPivot(arr,l,mid-1)
        return findPivot(arr,mid+1,h)
    
    return -1


def f():
    n = len(arr); 
    pivot_idx = findPivot(arr,0,len(arr)-1)
    
    print(pivot_idx)
    if arr[0] > key:
        return bin_search(arr,pivot_idx+1,len(arr)-1,key)
    return bin_search(arr, 0, pivot_idx, key)

print(f())