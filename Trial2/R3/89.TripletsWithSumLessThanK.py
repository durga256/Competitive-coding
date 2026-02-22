arr = [5, 1, 3, 4, 7]
K = 12

arr = [-2, 0, 1, 3]
K = 2.

def f():
    arr.sort()
    print(arr)
    n = len(arr)
    res = 0
    for i in range(len(arr)):
        curr_sum = K - arr[i]
        j = i+1; k = n-1
        while k > i and j < k:
            if arr[j] + arr[k] >= curr_sum:
                k -= 1
            else:
                print(arr[i],arr[j],arr[k])
                res += k-j
                j += 1

    print(res)

f()

