arr = [12, 11, 13, 5, 6]
arr = [6,1,2,4]

def insertion_sort():
    n = len(arr); j = 0
    for i in range(1,n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

    print(arr)

insertion_sort()

