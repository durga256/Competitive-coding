arr = [3, 1, 3]
#arr = [4, 3, 6, 2, 1, 1]

def findTwoElement(arr, n): 
    # code here
    sum_set = sum(set(arr))
    return [sum(arr)-sum_set,n*(n+1)//2 - sum_set]

def f():
    d = set(arr)
    i = 0; missing = -1; duplicate = -1
    while i < len(arr):
        if arr[i] != i+1:
            if arr[arr[i]-1] == arr[i]:
                duplicate = arr[i]
                break
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            i -= 1
        i += 1

    for i in range(1,len(arr)+1):
        if i not in d:
            missing = i
    
    print(missing)
    print(duplicate)

f()

    