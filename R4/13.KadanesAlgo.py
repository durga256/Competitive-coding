# Example:

# Input: [-3, -4, 5, -1, 2, -4, 6, -1]
# Output: 8
# Explanation: Subarray [5, -1, 2, -4, 6] is the max sum contiguous subarray with sum 8.

# Input: [-2, 3, -1, 2]
# Output: 4
# Explanation: Subarray [3, -1, 2] is the max sum contiguous subarray with sum 4.

nums = [-3, -4, 5, -1, 2, -4, 6, -1]

def max_sum_subarr():
    max_sum_sofar = nums[0]
    max_sum_current = nums[0]
    for i in range(1,len(nums)):
        max_sum_current += nums[i]
        if max_sum_current > max_sum_sofar:
            max_sum_sofar = max_sum_current
        if max_sum_current < 0:
            max_sum_current = 0

    return max_sum_sofar

print(max_sum_subarr())