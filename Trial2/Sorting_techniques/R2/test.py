arr = [12, 11, 13, 5, 6, 7]

def heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        arr = heapify(arr, n, largest)

    return arr


def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        arr = heapify(arr, i, 0)

    print(arr)

heap_sort(arr)


    
