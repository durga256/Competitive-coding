arr = [3, 1, 3]
#arr = [4, 3, 6, 2, 1, 1]

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

def f2():
    n = len(arr)
    sum_of_arr = sum(arr)
    repeating = sum_of_arr-sum(set(arr))
    missing = n*(n+1)//2 - sum_of_arr + repeating
    print(repeating, missing)

f2()

    