arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
arr = [0,0,5,5,0,0]
arr = [6,-1,-3,4,-2,2,4,6,-12,-7]

def f():
    d = {}; curr_sum = 0; d[curr_sum] = [0]
    res = []
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum not in d:
            d[curr_sum] = [i+1]
        else:
            for j in d[curr_sum]:
                res.append([j,i])
            d[curr_sum].append(i+1)

    print(d)
    print(res)

f()
