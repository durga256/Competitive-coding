arr  = [2, 4, 8, 10, 12, 14]

arr = [14,12,10,8,4,2]
arr = [49, 59, 69, 79, 89, 99, 109, 129]

def bin_search(arr, l, h,is_increasing):
    if l <= h:
        mid = (h-l)//2+l

        if mid > 0 and mid < len(arr) and arr[mid]-arr[mid-1] != arr[mid+1]-arr[mid]:
            if is_increasing:
                if arr[mid]-arr[mid-1] > arr[mid+1]-arr[mid]:
                    return arr[mid+1]-arr[mid]+arr[mid-1]
                else:
                    return arr[mid]-arr[mid-1]+arr[mid]
            else:
                if arr[mid]-arr[mid-1] < arr[mid+1]-arr[mid]:
                    return arr[mid+1]-arr[mid]+arr[mid-1]
                else:
                    return arr[mid]-arr[mid-1]+arr[mid]
            
        return bin_search(arr,l, mid-1,is_increasing) or bin_search(arr,mid+1, h,is_increasing)
    return False


def f():
    is_increasing = False
    n = len(arr)
    if arr[n-1]-arr[0] > 0: is_increasing = True
    print(bin_search(arr,0,len(arr)-1, is_increasing))

f()