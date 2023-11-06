arr = [1, 1, 1, 1]; K = 2
        

def pairs():
    d = {}; result = 0
    for i in range(len(arr)):
        if K-arr[i] in d.keys():
            result += d[K-arr[i]]
        if arr[i] in d.keys():
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    print(d)
    print(result)



pairs()
