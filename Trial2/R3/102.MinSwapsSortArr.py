def minSwaps(arr):
		#Code here
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = i
    temp = sorted(arr)
    res = 0
    for i in range(len(arr)):
        if arr[i] != temp[i]:
            res += 1
            idx = d[temp[i]]
            arr[i], arr[idx] = arr[idx], arr[i]
            d[arr[idx]] = idx

    return res

nums = [8,3,14,17,15,1,12]
nums = [7,16,14,17,6,9,5,3,18]
print(minSwaps(nums))