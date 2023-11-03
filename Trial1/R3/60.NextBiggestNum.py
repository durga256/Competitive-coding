n = 12222333

def next():
    nums = list(str(n)); pivot_idx = -1
    for i in range(len(nums)-1,0,-1):
        if nums[i] > nums[i-1]:
            pivot_idx = i - 1
            break

    if pivot_idx == -1:
        return -1

    ideal_ele_idx = pivot_idx + 1
    for i in range(pivot_idx + 2, len(nums)):
        if nums[i] > nums[pivot_idx] and nums[i] <= nums[ideal_ele_idx]:
            ideal_ele_idx = i

    nums[ideal_ele_idx], nums[pivot_idx] = nums[pivot_idx], nums[ideal_ele_idx]
    
    #reverse arr
    i = pivot_idx + 1; j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1; j -= 1

    print(nums)
    res = ""
    for i in nums:
        res += str(i)

    print(int(res))


print(next())

