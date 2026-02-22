arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]

def union():
    result = []
    i = 0; j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1; j += 1
        else:
            result.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    print(result)

def intersection():
    result = []
    i = 0; j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1; j += 1
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    print(result)

union()
intersection()