arr= [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
lowVal = 14; highVal = 20
arr=[76, 8, 75, 22, 59, 96, 30, 38, 36]
lowVal=44; highVal=62

def threeway():
    n = len(arr)
    low = 0; high = len(arr) - 1; i = 0
    while i <= high:
        if arr[i] < lowVal:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
        elif arr[i] > highVal:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1; i -= 1
        i += 1
        print(arr, i, low, high)
    print(arr)

threeway()
