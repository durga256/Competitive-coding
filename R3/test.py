height = [0,1,0,2,1,0,1,3,2,1,2,1]

def find_water():
    max_flank = 0; right_flank = [0 for i in range(len(height))]
    for i in range(len(height)-1,-1,-1):
        right_flank[i] = max_flank
        if max_flank < height[i]:
            max_flank = height[i]
    
    left_flank = 0; res = 0
    for i in range(len(height)):
        temp = min(right_flank[i],left_flank) - height[i]
        if temp > 0:
            res += temp
        if left_flank < height[i]:
            left_flank = height[i]

    print(right_flank)

    return res

print(find_water())