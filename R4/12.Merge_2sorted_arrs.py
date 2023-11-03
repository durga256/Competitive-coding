arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]

def merge_sorted():
    n = len(arr1); m = len(arr2)
    i = n-1; j = 0
    while i >= 0 and j < m:
        if arr1[i] < arr2[j]:
            break
        if arr1[i] > arr2[j]:
            temp = arr2[j]
            arr2[j] = arr1[i]
            j += 1

        k = i-1
        while k >= 0 and arr1[k] > temp:
            arr1[k+1] = arr1[k]
            k -= 1
        arr1[k+1] = temp
    arr2.sort()
    print(arr1)
    print(arr2)

def merge_sorted_2():
    n = len(arr1); m = len(arr2)
    i = 0; j = 0; k = n-1
    while i <= k and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        else:
            arr2[j], arr1[k] = arr1[k], arr2[j]
            j += 1; k -= 1

    arr2.sort()
    arr1.sort()


merge_sorted_2()


