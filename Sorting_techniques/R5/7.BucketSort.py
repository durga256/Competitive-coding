x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
    return arr


def bucket_sort():
    output = [[],[],[],[],[],[],[],[],[],[]]
    res = []
    for i in range(len(x)):
        output[int(x[i]*10)].append(x[i])
    
    print(output)
    for i in range(len(output)):
        output[i] = insertion_sort(output[i])

    print(output)
    for i in output:
        for j in i:
            res.append(j)

    print(res)



bucket_sort()