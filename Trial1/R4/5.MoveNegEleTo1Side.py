# move neg elements to one side
nums = [0,-1,0,0,0,-74,23,45,-2,-2,-3,45,-1]

def move_negs():
    # track next position of negative element using i
    i = 0
    while nums[i] < 0:
        i += 1
    
    for j in range(i, len(nums)):
        if nums[j] < 0:
            nums[i], nums[j] = nums[j], nums[i]
            i+= 1
    print(nums)

move_negs()

