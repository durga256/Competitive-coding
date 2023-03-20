nums = [-75,-35,-27,-7,-6,-5,0,4,56]

#naive solution
#O(n) space O(1)
# temp = nums[0]
# for i in range(len(nums)-1):
#     nums[i] = nums[i+1]

# nums[len(nums) - 1] = temp
# print(nums)

#how to rotate by the input value times? Say rotate 3 times.
#O(kn)
k = int(input("Enter number of times to rotate: "))

# i = 0
# while i < k:
#     temp = nums[0]
#     for j in range(len(nums)-1):
#         nums[j] = nums[j+1]
#     nums[len(nums) - 1] = temp
#     i += 1

# print(nums)

#optimize?
#O(n) space O(n)
# result = []
# for i in range(k,len(nums)):
#     result.append(nums[i])
# for i in range(k):
#     result.append(nums[i])
# print(result)

#optimize?
#nums = [-75,-35,-27,-7,-6,-5,0,4,56]
#O(k) and space O(1) for swap
i = 0
while i < k:
    nums[k+i], nums[i] = nums[i], nums[k+i]
    nums[k+i], nums[len(nums)-(k-i)] = nums[len(nums)-(k-i)], nums[k+i]
    i += 1

print(nums)