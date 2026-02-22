arr = [4, 2, -3, 1, 6]

def zeroSumSubArr():
    n = len(arr); d = {}; curr_sum = 0
    d[curr_sum] = 1
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum in d.keys():
            return True
        d[curr_sum] = 1
        
    return False

print(zeroSumSubArr())