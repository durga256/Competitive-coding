#Find the triplet that sum to a given value

arr = [589,343,609,61,222,759,955,889,147,691,950,844,431,621,749,68,537,784,36,227,186,39,854,630,225,749,924,360,258,767,945,956,319,727,412,26,356,2,550,497,585,516,965,343,76,914,143,197,949,73]; 
target_sum= 1541

def find_trip():
    for i in range(len(arr)):
        s = []
        curr_sum = target_sum - arr[i]
        for j in range(i+1, len(arr)):
            if curr_sum - arr[j] in s:
                return (arr[i], arr[j], curr_sum - arr[j])
            s.append(arr[j])
    
def find_trip_noset():
    for i in range(len(arr)):
        curr_sum = target_sum - arr[i]
        j = 0; k = len(arr) - 1
        while j < k:
            if arr[j] + arr[k] == curr_sum:
                return (arr[i], arr[j], arr[k])
            elif arr[j] + arr[k] > curr_sum:
                k -= 1
            else:
                j += 1
    return []

def threeSum_alltrip(nums):
        nums.sort(); res = set()
        for i in range(len(nums)):
            curr_sum = 0 - nums[i]
            j = i+1; k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == curr_sum:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1; k -= 1
                elif nums[j] + nums[k] > curr_sum:
                    k -= 1
                else:
                    j += 1

        return list(res)

print(find_trip())