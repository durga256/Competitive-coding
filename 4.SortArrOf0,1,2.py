nums = [1,0,0,0,1,2,2,2,1,0,1,1,0,1,2,0,2,1,0]

#naive solution
#complexity O(2n)
# l = [0,0] #count of each
# for i in nums:
#     if i == 0:
#         l[0] += 1
#     if i == 1:
#         l[1] += 1

# print("Original arr: ", nums)
# for i in range(len(nums)):
#     if i < l[0]:
#         nums[i] = 0
#     if i >= l[0] and i < l[1]+l[0]:
#         nums[i] = 1
#     elif i >= l[1]+l[0]:
#         nums[i] = 2
# print("Sorted arr: ", nums)

#one pass solution
#this is the dutch national flag problem. 
# but all the 0s/1s/2s are considered unique here so 0s are swapped with each other and so on. Any optimization?
# O(n)
low = 0
i = 0
high = len(nums) - 1
#nums = [1,0,0,0,1,2,2,2,1,1,1,0,1,2,2,1,0]
while i < high:
    if nums[i] == 0:
        nums[low], nums[i] = nums[i], nums[low]
        low += 1
    if nums[i] == 2:
        nums[high], nums[i] = nums[i], nums[high]
        high -= 1
        i -= 1
    i += 1

print(nums)
    


    
    
    
    


    
    


