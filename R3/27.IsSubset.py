#Find whether an array is a subset of another array

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

def findif():
    d = {}
    for i in arr1:
        d[i] = 0
    
    for i in arr2:
        if i not in d.keys():
            return False
    return True

print(findif())