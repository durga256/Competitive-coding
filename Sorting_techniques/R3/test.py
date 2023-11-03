arr = [12, 11, 13, 5, 6, 7]

def heapify(arr, n, i):
    largest = i
    left_child = 2*i + 1
    right_child = 2*i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        arr = heapify(arr, n, largest)
    
    return arr

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        arr = heapify(arr, n, i)

    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        arr = heapify(arr, i, 0)

    print(arr)

heap_sort(arr)