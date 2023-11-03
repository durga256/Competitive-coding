nums = [2,7,11,13,9,5,4]
target = 9
def binary_search(num, low, high):
    if low >= high:
        return -1
    mid_idx = (high-low)//2
    if nums[mid_idx] == num:
        return mid_idx
    if nums[mid_idx] < num:
        return binary_search(num, mid_idx+1, high)
    else:
        return binary_search(nums, low, mid_idx-1)


def find_pairs():
    nums.sort()
    res = []
    for i in range(len(nums)):
        idx = binary_search(target - nums[i], i, len(nums)-1)
        if idx != -1:
            res.append([nums[i], nums[idx]])
    print(res)

find_pairs()
        