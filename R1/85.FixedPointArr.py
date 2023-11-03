arr = [-10, -5, 0, 3, 7]
#arr = [0, 2, 5, 8, 17]
#arr = [-10, -5, 3, 4, 7, 9]

def bin_search(arr,low,high):
    if low < high:
        mid = (high-low)//2+low

        if arr[mid] == mid:
            return mid
        elif arr[mid] < 0 or arr[mid] < mid:
            return bin_search(arr,mid+1,high)
        elif arr[mid] >= len(arr) or arr[mid] > mid:
            return bin_search(arr, low, mid-1)
    
    return -1

# def binarySearch(arr, low, high): 
#     if high >= low : 
          
#         mid = low + (high - low)//2
#         if mid == arr[mid]:
#             return mid 
#         res = -1
#         if mid + 1 <= arr[high]:
#             res = binarySearch(arr, (mid + 1), high) 
#         if res !=-1: 
#             return res
#         if mid-1 >= arr[low]:
#             return binarySearch(arr, low, (mid -1)) 
      
  
#     # Return -1 if there is no Fixed Point 
#     return -1

#print(binarySearch(arr, 0,len(arr)-1))
print(bin_search(arr,0,len(arr)-1))
