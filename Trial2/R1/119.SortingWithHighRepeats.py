arr = [10, 7, 8, 9, 1, 5]
arr = [3,1,2,4]
arr = [3,4 ,1, 6, 2, 5]
def partition(arr, low, high):
    pivot = arr[high]
    j = low; k = high-1
    while j <= k:
        if arr[j] < pivot:
            arr[j], arr[low] = arr[low], arr[j]
            low += 1
        elif arr[j] > pivot:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1; j-= 1
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


