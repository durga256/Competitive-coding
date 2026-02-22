ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]

def f(ar1, ar2):
    n = len(ar1); m = len(ar2)
    if n > m:
        return f(ar2,ar1)
    
    start = 0
    end = n
    real_arr_mid_idx = (n+m+1)//2
    while start  <= end:
        mid = (start + end)//2
        leftAsize = mid
        leftBSize = real_arr_mid_idx - mid

        leftA = ar1[leftAsize - 1] if leftAsize > 0 else float('-inf')
        leftB = ar2[leftBSize - 1] if leftBSize > 0 else float('-inf')
        rightA = ar1[leftAsize] if leftAsize < n else float('inf')
        rightB = ar2[leftBSize] if leftBSize < m else float('inf')

        if leftA <= rightB and leftB <= rightA:
            if (m+n) %2 == 0:
                return (max(leftA, leftB)+min(rightA, rightB))/2
            return max(leftA, leftB)
        elif leftA  > rightB:
            end = mid -1
        else:
            start = mid + 1

print(f(ar1, ar2))
