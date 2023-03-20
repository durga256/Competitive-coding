# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

nums = [1, 2, 3, 6, 5, 4]

def next_permutation(nums):
    n = len(nums)
    for i in range(n-1, 0, -1):
        if nums[i-1] < nums[i]:
            val = nums[i-1]
            idx_to_reverse = i #also the index of val + 1
            break
    
    if val != -1: # to handle the case where we have the max lexicographical val possible
        for i in range(n-1, 0, -1):
            if nums[i] > val:
                nums[i], nums[idx_to_reverse-1] = nums[idx_to_reverse-1], nums[i]
                break
        nums[idx_to_reverse:] = reversed(nums[idx_to_reverse:])
    else:
        nums = reversed(nums)

next_permutation(nums)
print(nums)

def find_next_permutation():
    pivot_idx = -1
    for i in range(len(nums)-1, 0, -1):
        if nums[i-1] < nums[i]:
            pivot_idx = i
            break
    if pivot_idx == -1:
        nums.reverse()
        return nums
    
    for i in range(len(nums)-1, -1, -1):
        if nums[i] > nums[pivot_idx - 1]:
            min_decreasing_idx = i

    nums[pivot_idx-1], nums[min_decreasing_idx] = nums[min_decreasing_idx], nums[pivot_idx-1]
    nums[pivot_idx:] = reversed(nums[pivot_idx:])
    print(min_decreasing_idx)
