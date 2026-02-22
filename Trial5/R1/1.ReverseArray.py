arr = [1,2,3,4,5,6]
# arr = [1,2,3,4,5]

#O(n/2) ~ O(n) space- O(1) but in-place
def pointer_reverse():
    i = 0; j = len(arr)-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1; j -= 1
    
    return arr

#O(n) space-O(1) but in-place
def python_reverse():
    arr.reverse() # return none
    return arr

#O(n) space- O(n) not in-place
def slice_reverse():
    return arr[::-1]

#O(n/2) ~ O(n) space-O(1) in place
def iter_reverse():
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr


print(arr)
print(pointer_reverse())
print(iter_reverse())
print(python_reverse())
print(slice_reverse())


