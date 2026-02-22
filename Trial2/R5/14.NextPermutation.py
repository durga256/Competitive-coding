nums = [1, 2, 3, 6, 5, 4]
#nums = [2,3,1,3,3]

def next_perm(nums):
    n = len(nums);  pivot_idx = -1
    for i in range(n-1,0,-1):
        if nums[i] > nums[i-1]:
            pivot_idx = i-1
            break

    min_idx = pivot_idx + 1
    for i in range(pivot_idx+1,n):
        if nums[i] > nums[pivot_idx] and nums[i] <= nums[min_idx]:
            min_idx = i

    if pivot_idx != -1:
        nums[pivot_idx], nums[min_idx] = nums[min_idx], nums[pivot_idx]
    else:
        nums[0:] = reversed(nums[0:])
        return nums
    
    nums[pivot_idx+1:] = reversed(nums[pivot_idx+1:])
    return nums

print(next_perm(nums))