def f(x,l,h):
    while l <= h:
        mid = (l+h)//2

        if mid*mid == x:
            return mid
        if mid*mid < x:
            l = mid + 1
            ans = mid
        else:
            h = mid -1

    return ans

print(f(80,0,100))
        
