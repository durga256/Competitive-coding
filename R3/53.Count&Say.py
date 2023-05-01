n = 4
#https://leetcode.com/problems/count-and-say/
#3322251

def integer_to_say(nums):
    count = 1; i = 1; prev = nums[0]; res = ""
    while i < len(nums):
        if nums[i] == prev:
            count += 1
        else:
            res += str(count) + str(prev)
            prev = nums[i]
            count = 1
        i += 1
    
    res += str(count) + str(prev)
    return res


def coun():
    k = "1"
    for i in range(n-1):
        k = integer_to_say(k)
        print(k)



coun()
