# Rearrange the array in alternating positive and negative items
# with O(1) extra space
# Input:  arr[] = {1, 2, 3, -4, -1, 4}
# Output: arr[] = {-4, 1, -1, 2, 3, 4}

# Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

arr = nums = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
def find_next_neg(start_idx):
    for i in range(start_idx+1, len(nums)):
        if nums[i] < 0:
            return i
    return -1

def find_next_pos(start_idx):
    for i in range(start_idx+1, len(nums)):
        if nums[i] > 0:
            return i
    return -1

def cyclically_rotate_arr(start_idx, end_idx):
    temp = nums[end_idx]
    for i in range(end_idx, start_idx, -1):
        nums[i] = nums[i-1]
    nums[start_idx] = temp
    print(nums)

def alt_neg_pos():
    #we know negs are at even indexes
    # pos are at odd indexes
    end_idx = -1
    for i in range(len(nums)):
        if i%2 == 0 and nums[i] > 0: 
            end_idx = find_next_neg(i)
        elif i%2 != 0 and nums[i] < 0:
            end_idx = find_next_pos(i)
        if end_idx != -1:
            cyclically_rotate_arr(i,end_idx)
            end_idx = -1

def rearr():
    outofPlace = -1
    print(arr)
    i = 0
    while i < len(arr):
        if outofPlace != -1:
            if (arr[outofPlace] < 0 and arr[i] > 0) or (arr[outofPlace] > 0 and arr[i] < 0):
                print(outofPlace, i)
                cyclically_rotate_arr(outofPlace, i)
                outofPlace = -1; i-= 1

        else:
            if (arr[i] < 0 and i % 2 == 0) or (arr[i] > 0  and i % 2 != 0):
                outofPlace = i
        i += 1
    print(arr)

rearr()


            






    

alt_neg_pos()
print(nums)
