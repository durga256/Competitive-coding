from collections import Counter
arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
k = 4

def findndivk():
    res = 0
    d = Counter(arr)
    n = len(arr)
    for i in d:
        if d[i] > n//k:
            res += 1

    print(d, res)

findndivk()
