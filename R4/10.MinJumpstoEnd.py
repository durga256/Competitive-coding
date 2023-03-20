# Given an array arr[] where each element represents the max number of 
# steps that can be made forward from that index. 
# The task is to find the minimum number of jumps to reach the
# end of the array starting from index 0. If the end isn’t reachable, 
# return -1.
arr = [3,1,1,1,1]

def min_jumps_to_end():
    n = len(arr)
    arr[n-1] = 0
    for i in range(n-2, -1,-1):
        if arr[i] >= n - i + 1:
            arr[i] = 1
        else:
            temp_min = 10001
            for k in range(arr[i]):
                if i+k+1 < n and arr[i+k+1] < temp_min and arr[i+k+1] >= 0:
                    temp_min = arr[i+k+1]
            if arr[i] <= 0:
                arr[i] = -1
            else:
                arr[i] = temp_min + 1

min_jumps_to_end()
print(arr)

