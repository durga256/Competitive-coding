nums = [2,3,-2,4]
nums = [-2,0,-1]
# nums = [0,1]
# nums = [3,-1,4]
# nums = [-3,-1,-1]

def max_product():
    pos_max = 1; neg_max = 1; max_sofar = nums[0]
    for i in range(len(nums)):
        if nums[i] < 0:
            pos_max, neg_max = neg_max, pos_max
        pos_max = max(nums[i],pos_max*nums[i])
        neg_max = min(nums[i],neg_max*nums[i])
        max_sofar = max(max_sofar, pos_max)
    print(max_sofar)

max_product()
def maxProduct(nums) -> int:
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(nums + B)
        