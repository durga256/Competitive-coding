arr = [10, 7, 8, 9, 1, 5]

def partition(arr, low, high):
    pivot = arr[high]

    j = low
    while j <= high:
        if arr[j] < pivot:
            arr[low], arr[j] = arr[j], arr[low]
            low += 1
        elif arr[j] > pivot:
            arr[high], arr[j] = arr[j], arr[high]
            high -= 1; j-= 1
        j += 1
    print(arr)
    return low

def f(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)
        f(arr, low, pi-1)
        f(arr, pi+1, high)

f(arr,0,len(arr)-1)
print(arr)