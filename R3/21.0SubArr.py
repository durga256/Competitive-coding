#Find if there is any subarray with sum equal to 0
nums = [6, 3, -1, -3, 4, -2, 2]

def find_sub():
    d = {}; curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum in d.keys():
            d[curr_sum].append(i)
        else:
            d[curr_sum] = [i]
    print(d)
    #for cases where 0 is the element, then [0] and all [0,0], [0,0,0] will be subarrs
    for i in d.keys():
            temp = []
            if i == 0:
                for j in range(len(d[i])):
                    res.append([d[i][0], d[i][j]])
    res = []
    for i in d.values():
        if len(i) > 1:
            for j in range(len(i)-1):
                for k in range(j+1, len(i)):
                    res.append((i[j]+1, i[k]))

    print(res)
    return len(res)

find_sub()
    