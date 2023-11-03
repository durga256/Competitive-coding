nums = [3,1,-2,-5,2,-4]
nums = [-1,1]
nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]

def f():
    res = [0]*len(nums)
    neg_index = 1; pos_index = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            res[neg_index] = nums[i]
            neg_index += 2
        else:
            res[pos_index] = nums[i]
            pos_index += 2

    print(res)

f()