arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
k = 4

def findndivk():
    d = {}; res = 0
    for i in range(len(arr)):
        if arr[i] in d.keys():
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    
    for i in d.keys():
        if d[i] > len(arr)//k:
            res += 1

    print(d, res)

findndivk()
