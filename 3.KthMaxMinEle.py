arr = [1,2,67,89,5,4,-1,0]

#naive soln - sort
#complexity - O(nlogn)

arr.sort()
k = int(input("Enter k:"))

print(arr)
print("Kth Min element: ", arr[k-1])
print("Kth Max element: ", arr[-1*k])



