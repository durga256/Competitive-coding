import sys
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

#naive
def min_jumps(a, n, curr_step, no_steps):
    if curr_step >= n-1:
        return no_steps
    
    min_val = sys.maxsize
    no_steps += 1
    for i in range(curr_step, a[curr_step]+curr_step):
        temp = min_jumps(a,n,i+1,no_steps)
        if temp < min_val:
            min_val = temp

    return min_val

#optimised
def min_jumps_iter(a):
    cur_end = 0; cur_max = 0; ans = 0
    for i in range(len(a) - 1):
        cur_max = max(cur_max, a[i]+i)

        if i == cur_end:
            ans += 1
            cur_end = cur_max


    return ans


print(min_jumps(arr, len(arr), 0, 0))
print(min_jumps_iter(arr))

