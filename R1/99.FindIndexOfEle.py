arr = [4, 5, 6, 7, 6]; k = 1; x = 9

def f():
    if x in arr:
        return arr.index(x)
    return -1

print(f())