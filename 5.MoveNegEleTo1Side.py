nums = [0,-1,0,0,0,-74,23,45,-2,-2,-3,45,-1]

#O(n) solution
last_neg_element = 0
for i in range(len(nums)):
    if nums[i] < 0:
        nums[i], nums[last_neg_element] = nums[last_neg_element], nums[i]
        last_neg_element += 1

print(nums)