nums = [1,3,4,2,2]

def find_dup(a):
    n = len(a)
    for i in range(n):
        if nums[abs(nums[i])-1] < 0:
            return abs(nums[i])
        nums[abs(nums[i])-1] = -1*nums[abs(nums[i])-1]

    
print(find_dup(nums))