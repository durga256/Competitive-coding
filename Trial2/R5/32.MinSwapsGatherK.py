arr = [2, 1, 5, 6, 3]; k = 3
arr = [2, 7, 9, 5, 8, 7, 4]; k = 5

def min_swap():
    window_size = 0
    for i in range(len(arr)):
        if arr[i] <= k:
            window_size += 1

    bad = 0; i = 0
    while i < window_size:
        if arr[i] > k:
            bad += 1
        i += 1
    res = bad
    for i in range(1, len(arr)-window_size+1):
        if arr[i-1] > k:
            bad -= 1
        if arr[i+window_size-1] > k:
            bad += 1
        res = min(res, bad)

    print(res)

min_swap() 