# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

#Example 3:
# Input: nums = [2,2,2,2,2]
# Output: 2
nums = [1,3,4,2,2]

#O(n^2)
def find_duplicate_naive():
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
            
# there is no 0 in the array. use 0th index to store the duplicate
# basically put the index values into that pos and when clash report
# check if 0th index values matches with another index 
def find_duplicate():
    while nums[0] != nums[nums[0]]:
        nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
    return nums[0]


#mark all the indexes that are the element value to be -ve
# eg [1,3,4,2,2]. mark arr[abs(arr[0])] => arr[1] => -3
# then when the dup comes in. the index would already be marked neg. so thats ur answer
def find_dup_neg_marking(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])] > 0:
            arr[arr[i]] = -1*arr[arr[i]]
        else:
            print(arr)
            return arr[i]
        

    

print("The duplicate num is: ", find_dup_neg_marking(nums))