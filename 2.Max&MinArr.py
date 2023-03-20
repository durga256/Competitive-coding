arr = [1,2,67,89,5,4,-1,0]

#naive soln
#complexity: O(n)
max_ele = arr[0]
min_ele= arr[0]

for i in arr:
    if i > max_ele:
        max_ele = i
    if i < min_ele:
        min_ele = i

print("Max: ", max_ele)
print("Min: ", min_ele)