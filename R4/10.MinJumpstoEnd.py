# Given an array arr[] where each element represents the max number of 
# steps that can be made forward from that index. 
# The task is to find the minimum number of jumps to reach the
# end of the array starting from index 0. If the end isn’t reachable, 
# return -1.
nums = [2,2,0,0,4]

def min_jumps_to_end():
    n = len(nums)
    nums[n-1] = 0
    for i in range(n-2,-1,-1):
        if nums[i] >= n-1-i:
            nums[i] = 1
        else:
            min_sofar = nums[i+1]
            for j in range(1,nums[i]+1):
                min_sofar = min(min_sofar, nums[i+j])
            nums[i] = min_sofar + 1

    print(nums)

#min_jumps_to_end()

def opt():
    cur_end = 0; cur_max = 0; ans = 0
    for i in range(len(nums)-1):
        cur_max = max(cur_max, nums[i]+i)


        if i == cur_end:
            ans += 1
            cur_end = cur_max
    
    print(ans)

opt()

