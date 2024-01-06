arr = [4, 5, 6, 7, 6]; k = 1; x = 9

def f():
    i = 0
    n = len(arr)
    while i < n:
        if (arr[i] == x):
            return i
        
        #max to move atleast 1 step
        i = i + max(1, abs(arr[i]-x)//k)

    return -1

print(f())