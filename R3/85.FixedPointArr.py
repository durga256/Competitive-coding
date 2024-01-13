arr = [-10, -5, 0, 4, 7]
#arr = [0, 2, 5, 8, 17]
#arr = [-10, -5, 3, 4, 7, 9]

def bin_search(arr):
    l = 0; h = len(arr)-1
    while l <= h:
        mid = (l+h)//2
        if arr[mid] == mid+1:
            return mid+1
        elif arr[mid] < mid+1:
            l = mid+1
        else:
            h = mid -1
    return -1

print(bin_search(arr))
