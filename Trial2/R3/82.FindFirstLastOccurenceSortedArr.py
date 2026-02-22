#https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/

arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]; x = 5

def bin_search(arr, low, high, condition):
    if low > high:
        return -1
    
    mid = (high-low)//2+low

    if condition == 1:
        if (mid == 0 or arr[mid-1] != x) and arr[mid] == x:
            return mid
        elif arr[mid] >= x:
            return bin_search(arr,low,mid-1,condition)
        else:
            return bin_search(arr,mid+1,high,condition)
    else:
        if (mid == len(arr)-1 or arr[mid+1] != x) and arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bin_search(arr,low,mid-1,condition)
        else:
            return bin_search(arr,mid+1,high,condition)

def f():
    temp1 = bin_search(arr,0,len(arr)-1,1)
    temp2 = bin_search(arr,0,len(arr)-1,0)
    print(temp1,temp2)


f()

