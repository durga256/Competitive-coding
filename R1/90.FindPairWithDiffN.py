arr = [5, 20, 3, 2, 50, 80]; n = 78

def f():
    d = {}

    for i in range(len(arr)):
        d[arr[i]] = 1

    for i in range(len(arr)):
        if arr[i] + n in d:
            return True
        
    return False
        
    