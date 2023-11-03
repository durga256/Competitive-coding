def minSwaps(nums):
		#Code here
    temp = nums.copy(); res = 0
    temp.sort(); d = {}
    for i in range(len(nums)):
        d[nums[i]] = i
    for i in range(len(nums)):
        if nums[i] != temp[i]:
            res += 1
            true_idx = d[temp[i]]
            d[nums[i]] = true_idx
            nums[true_idx], nums[i] = nums[i], nums[true_idx]
        print(nums)
    return res

nums = [8,3,14,17,15,1,12]
nums = [7,16,14,17,6,9,5,3,18]
print(minSwaps(nums))