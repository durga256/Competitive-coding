# Case A) A number is more than one higher than the ideal; for example, i = 3, A[i] = 5.

# When i is 3, that means we've seen 3 numbers already, yet there are 5 numbers that are less than 5. 
# That then means that there are at least 2 numbers that are less than 5 that we have not yet seen, 
# which in turn means that there are at least 2 global inversions triggered by this one deviation.

# Case B) A number is more than one lower than the ideal; for example, i = 3, A[i] = 1.

# When i is 3, that means we've seen 3 numbers already, yet only 1 number is less than 1. 
# That then means that at least 2 of the numbers we've seen are higher than 1, 
# which in turn means that we've already triggered at least 2 gobal inversions because 
# of this one deviation.

# note for the below soln all integers in the arr must unique
nums = [1,2,0,3]
def count_inversions_unique():
    for i in range(len(i)):
        if i - nums[i] > 1 or i - nums[i] < -1: return False
        return True
#says if global inversions == local inversion

# note for the below soln all integers in the arr must unique

def inversions():
    inv = 0
    for i in range(len(nums)):
        if nums[i] - i> 1:
            inv += nums[i] - i
    print(inv)
    #pass 216/226 testcases but bit buggy. 

#inversions()
    
#count inversions normal - O(nlogn)
nums = [1,2,0,3]
ans = 0
def merge_sort(arr):
    global ans
    if len(arr) > 1:
        mid_idx = len(arr)//2

        L = merge_sort(arr[:mid_idx])
        R = merge_sort(arr[mid_idx:])
        i = 0; j = 0; k = 0
        while i < len(L) and j < len(R):
            if R[j] < L[i]:
                arr[k] = R[j]
                k += 1; j += 1; ans += mid_idx-i
            else:
                arr[k] = L[i]
                k += 1; i += 1
        while i < len(L):
            arr[k] = L[i]
            k += 1; i += 1
        while j < len(R):
            arr[k] = R[j]
            k += 1; j += 1
        return arr
    else:
        return arr


print(merge_sort(nums))
print(ans)

    

