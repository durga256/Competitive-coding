arr = [10, 7, 8, 9, 1, 5]
def partition(arr, low, high):
    pivot = arr[high]
    j = low
    while j < high:
        if arr[j] <= pivot:
            arr[j], arr[low] = arr[low], arr[j]
            low += 1
        j += 1
    arr[low], arr[high] = arr[high], arr[low]
    print(arr)
    return low
    
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

quickSort(arr, 0, len(arr)-1)
print(arr)


