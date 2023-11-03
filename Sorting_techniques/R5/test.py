arr = [12, 11, 13, 5, 6]
arr = [6,1,2,4]

def f():
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    print(arr)

f()