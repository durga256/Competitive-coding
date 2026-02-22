arr = [12, 11, 13, 5, 6, 7]

def heapify(arr, i, n):
    largest = i
    left_child = 2*i + 1
    right_child = 2*i + 2

    if left_child < n and arr[largest] < arr[left_child]:
        largest = left_child
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest, n)

def heap_sort():
    n = len(arr)

    for i in range(n//2-1, -1,-1):
        heapify(arr, i, n)
        print(arr)

    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
        #print(arr)

    #print(arr)

heap_sort()
