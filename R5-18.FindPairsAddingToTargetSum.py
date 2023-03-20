nums = [2,7,11,13,9, 5, 4]
target = 9

def find_pairs():
    d = {}
    all_pairs = []
    for i in range(len(nums)):
        d[target - nums[i]] = i

    for i in range(len(nums)):
        if nums[i] in d:
            if d[nums[i]] != -1 and d[nums[i]] != i:
                all_pairs.append([nums[d[nums[i]]], nums[i]])
                d[nums[d[nums[i]]]] = -1
    return all_pairs


print(find_pairs())


