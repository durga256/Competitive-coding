nums = [5, 6, 7, 11, 12, 13]
nums.sort()
def binary_Search(nums, l, h, num):
    if h - l <1:
        return -1
    mid_idx = (l+h)//2

    if nums[mid_idx] == num:
        return mid_idx
    
    if nums[mid_idx] < num:
        return binary_Search(nums, mid_idx+1, h, num)
    return binary_Search(nums, l, mid_idx, num)



print(binary_Search(nums, 0, len(nums), 11))