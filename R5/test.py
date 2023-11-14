arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
k = 4

def f():
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    res = []
    for i in d:
        if d[i] > len(arr)//k:
            res.append(i)

    print(res)

f()
