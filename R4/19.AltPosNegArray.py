nums = [3,1,-2,-5,2,-4]
nums = [-1,1]
nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]

def rearrange():
    result = [0]*len(nums)
    pos_index = 0; neg_index = 1
    for i in range(len(nums)):
        if nums[i] < 0:
            result[neg_index] = nums[i]
            neg_index += 2
        else:
            result[pos_index] = nums[i]
            pos_index += 2



    print(result)

rearrange()

def rearrangeArray(nums):
    i = 0; low_pos = 0; low_neg = 1; n = len(nums)
    while i < n:
        if i%2 == 0:
            if nums[i] > 0:
                low_pos += 2
            elif nums[i] < 0 and low_neg < n: 
                nums[low_neg], nums[i] = nums[i], nums[low_neg]
                low_neg += 2; i -= 1
        if i%2 != 0:
            if nums[i] < 0:
                low_neg += 2
            elif nums[i] > 0 and low_pos < n:
                nums[low_pos], nums[i] = nums[i], nums[low_pos]
                low_pos += 2; i -= 1
        i += 1
    return nums

print(rearrangeArray(nums))