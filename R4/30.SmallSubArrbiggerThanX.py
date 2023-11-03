arr = [1, 4, 45, 6, 0, 19]; x  =  51
def small_sub():
    curr_sum = 0; start = end = 0; min_len = len(arr)+1
    while end < len(arr):

        while end < len(arr) and curr_sum <=x:
            curr_sum += arr[end]
            end += 1

        while start <= end and curr_sum > x:
            min_len = min(min_len, end-start)
            curr_sum -= arr[start]
            start += 1

    print(min_len)

small_sub()
