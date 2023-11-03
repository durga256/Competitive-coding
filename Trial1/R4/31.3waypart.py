#Three way partitioning of an array around a given value

arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]; lowVal = 14; highVal = 20

def part():
    low_idx = 0; high_idx = len(arr) - 1; i = 0
    while i <= high_idx:
        if arr[i] < lowVal:
            arr[i], arr[low_idx] = arr[low_idx], arr[i]
            low_idx += 1
        elif arr[i] > highVal:
            arr[i], arr[high_idx] = arr[high_idx], arr[i]
            high_idx -= 1; i -= 1
        i += 1
        print(arr)
    
    print(arr)

part()