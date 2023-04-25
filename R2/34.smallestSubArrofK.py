#Smallest Subarray with sum greater than a given value
import sys
arr = [1, 4, 45, 6, 0, 19]; x  =  51
x = 7; arr = [2,3,1,2,4,3]

def small():
    ans = len(arr)
    for i in range(len(arr)):
        curr_sum = arr[i]; min_size = 1
        for j in range(i+1, len(arr)):
            if curr_sum > x:
                ans = min(ans, min_size)
                break
            curr_sum += arr[j]
            min_size += 1
    
    print(ans)

def small_opt():
    start = 0; end = 0; n = len(arr); curr_sum = 0; min_len = n + 1
    while end < n:

        while curr_sum < x and end < n:
            curr_sum += arr[end]
            end += 1
        
        while curr_sum >= x and start < n:
            min_len = min(min_len, end-start)
            print("current sum: ", curr_sum)

            curr_sum -= arr[start]
            start += 1

    if min_len == len(arr):
        return 0
    return min_len



small()
print(small_opt())