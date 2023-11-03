nums = [2,3,-2,4]
nums = [2,-5,-2,-4,3]

def max_prod():
    neg_result = pos_result = 1; max_sofar = nums[0]
    for i in range(len(nums)):
        if nums[i] < 0:
            pos_result, neg_result = neg_result, pos_result
        pos_result = max(nums[i], pos_result*nums[i])
        neg_result = min(nums[i], neg_result*nums[i])
        max_sofar = max(max_sofar, pos_result)
        print(pos_result, neg_result, max_sofar)
        if nums[i] == 0:
            neg_result = pos_result = 1

max_prod()
