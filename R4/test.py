# Example:

# Input: [-3, -4, 5, -1, 2, -4, 6, -1]
# Output: 8
# Explanation: Subarray [5, -1, 2, -4, 6] is the max sum contiguous subarray with sum 8.

# Input: [-2, 3, -1, 2]
# Output: 4
# Explanation: Subarray [3, -1, 2] is the max sum contiguous subarray with sum 4.

nums = [-3, -4, 5, -1, 2, -4, 6, -1]

def s():
    curr_sum = 0; max_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        max_sum = max(max_sum, curr_sum)
        curr_sum = max(curr_sum, 0)

    print(max_sum)

s()