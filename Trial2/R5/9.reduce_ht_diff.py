arr = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]; k = 5
# arr = [1,10]; k = 5

def find_min_ht_diff(arr):
    n = len(arr)
    arr = sorted(arr)
    ans = max(arr) - min(arr)
    for i in range(1, n):
        if arr[i] < k:continue
        temp_min = min(arr[0]+k, arr[i]-k)
        temp_max = max(arr[i-1]+k, arr[n-1]-k)
        ans = min(ans, temp_max-temp_min)

    print(ans)
    return ans


find_min_ht_diff(arr)
