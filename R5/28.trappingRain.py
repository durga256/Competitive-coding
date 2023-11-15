height = [4,2,0,3,2,5]

def trap():
    n = len(height)
    right_flank = [0]*len(height); max_value = height[n-1]
    for i in range(n-1,-1,-1):
        right_flank[i] = max_value
        max_value = max(max_value, height[i])

    print(right_flank)
    res = 0; left_flank = height[0]
    for i in range(1,n):
        left_flank = max(left_flank, height[i])
        res += max(0,min(right_flank[i],left_flank) - height[i])
        print(res)


trap()

    

