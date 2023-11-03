A = [3, 3, 4, 2, 4, 4, 2, 4]

def f():
    d = {}
    for i in A:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in d:
        if d[i] > len(A)//2:
            return i
        
    return -1
        

print(f())