def f(arr,l,h):
    if l <= h:
        mid = (l+h)//2

        if mid <h  and arr[mid+1] < arr[mid]:
            return mid
        elif mid > l and arr[mid-1] > arr[mid]:
            return mid-1
        if arr[l] >= arr[mid]:
            return f(arr, l,mid-1)
        return f(arr,mid+1, h)
    
nums = [2,2,7,5,4,3,2,2,1]
print(f(nums, 0, len(nums)-1))