def f(n):
    l = 1; h = max(1,n//2)
    while l <= h:
        mid = (l+h)//2
        sq = mid*mid
        if sq == n:
            return mid
        elif sq < n and (mid+1)*(mid+1) > n:
            return mid
        elif sq < n:
            l = mid+1
        else:
            h = mid-1

    return -1

print(f(80))
        
