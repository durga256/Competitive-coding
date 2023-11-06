nums = [3,1,-2,-5,2,-4]
nums = [-1,1]
nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]

def f():
    print(nums); i = 0
    low_pos = 0; low_neg = 1
    while i < len(nums):
        if i%2 == 0:
            if nums[i] > 0:
                low_pos += 2
            elif nums[i] < 0 and low_neg < len(nums):
                nums[i], nums[low_neg] = nums[low_neg], nums[i]
                low_neg += 2; i -= 1
        if i%2 != 0:
            if nums[i] < 0:
                low_neg += 2
            elif nums[i] > 0 and low_pos < len(nums):
                nums[i], nums[low_pos] = nums[low_pos], nums[i]
                low_pos += 2; i -= 1
        i += 1

    print(nums)

f()