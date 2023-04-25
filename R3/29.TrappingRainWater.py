nums = [0,1,0,2,1,0,1,3,2,1,2,1]
nums = [4,2,0,3,2,5]
nums = [0,7,1,4,6]

def sum_pos(res):
    tots = 0
    for i in res:
        if i > 0:
            tots += i
    return tots


def trap():
    left_flank = 0; res = []
    right_flanks = [0 for x in range(len(nums))]; right_flank_max = 0
    for i in range(len(nums) - 1, -1, -1):
        right_flanks[i] = right_flank_max
        if nums[i] > right_flank_max:
            right_flank_max = nums[i]


    for i in range(len(nums)):
        if left_flank < nums[i]:
            left_flank = nums[i]
        temp = min(left_flank, right_flanks[i]) - nums[i]
        if i == 5:
            print(left_flank, right_flanks[i], temp)
        if temp > 0:
            res.append(temp)
            continue
        res.append(-1)
    print(res)
    print(sum_pos(res))

trap()