def productExceptSelf(arr, n):
    #code here
    count_of_zeroes = 0
    product_of_arr = 1
    for i in arr:
        if i == 0:
            count_of_zeroes += 1
        else:
            product_of_arr *= i

    res = [0] * len(arr)
    if count_of_zeroes > 1:
        return res
    if count_of_zeroes == 1:
        idx = arr.index(0)
        res[idx] = product_of_arr
        return res
    for i in range(len(arr)):
        res[i] = product_of_arr//arr[i]

    return res

#if you couldnt divide?
def f2(arr):
    res = [1]*len(arr)
    curr = 1
    for i in range(len(arr)):
        res[i] *= curr
        curr *= arr[i]

    curr = 1
    for i in range(len(arr)-1,-1,-1):
        res[i] *= curr
        curr *= arr[i]

    return res
