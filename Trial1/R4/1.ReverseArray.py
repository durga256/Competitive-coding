#reverse arr
nums = [1,2,3,4,5,6,7]

#O(n)
for i in range(len(nums)//2):
    nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]

print(nums)
