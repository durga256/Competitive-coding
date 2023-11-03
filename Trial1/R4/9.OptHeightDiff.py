# Given the heights of N towers and a value of K, Either increase or decrease the height of every tower by K (only once) where K > 0. After modifications, the task is to minimize the difference between the heights of the longest and the shortest tower and output its difference.

# Examples: 

# Input: arr[] = {1, 15, 10}, k = 6
# Output:  Maximum difference is 5.
# Explanation: Change 1 to 7, 15 to 9 and 10 to 4. Maximum difference is 5 (between 4 and 9). We can’t get a lower difference.

# Input: arr[] = {1, 5, 15, 10}, k = 3   
# Output: Maximum difference is 8, arr[] = {4, 8, 12, 7}
# O(nlogn) - sorting
arr = [1, 15, 14]
k=3

# this only finds the difference. we cant know the transformed array
# O(nlogn) for sorting
def find_difference():
    sorted_arr = sorted(arr)
    n = len(arr)
    #the below 3 lines handles the case when all elements go through the same operation
    min_height = sorted_arr[0]
    max_height = sorted_arr[n-1]
    ans = max_height - min_height
    for i in range(n):
        min_height = min(sorted_arr[0]+k, sorted_arr[i]-k)
        max_height = max(sorted_arr[i-1]+k, sorted_arr[n-1]-k)
        ans = min(ans, max_height - min_height)

    return ans

# convert arr - move all elements closer to avg
#O(n)
        
def convert_arr():
    n = len(arr)
    min_height = arr[0]
    max_height = arr[0]

    # find min and max of arr to find avg
    for i in range(n):
        if min_height > arr[i]:
            min_height = arr[i]
        if max_height < arr[i]:
            max_height = arr[i]

    #the below 3 lines handles the case when all elements go through the same operation
    ans = max_height - min_height
    arr_avg = (max_height + min_height)/2

    for i in range(n):
        if arr[i] <= arr_avg:
            arr[i] += k
        else:
            arr[i] -= k

    min_height = arr[0]
    max_height = arr[0]

    for i in range(n):
        print(arr[i])
        if min_height > arr[i]:
            min_height = arr[i]
        if max_height < arr[i]:
            max_height = arr[i]

    ans = min(ans, max_height-min_height)
    return ans


print("max difference: ", find_difference())