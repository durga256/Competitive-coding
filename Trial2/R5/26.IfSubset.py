arr1 = [11, 1, 13, 21, 3, 7, 7]
arr2 = [11, 3, 7, 1, 5]

def if_subset():
    d = {}
    for i in range(len(arr1)):
        d[arr1[i]] = 0
    for i in range(len(arr1)):
        d[arr1[i]] += 1

    for i in range(len(arr2)):
        if arr2[i] in d and d[arr2[i]] > 0:
            d[arr2[i]] -= 1
        else:
            return False
        
    return True

print(if_subset())