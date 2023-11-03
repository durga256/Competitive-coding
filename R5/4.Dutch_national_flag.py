arr = [0,0,2,2,0,0,1,1,1,1,1,1,2,1,2,1,2,1,2,0,2,0,1]

def dutch(a):
    low = 0
    high = len(a) - 1
    i = 0
    while i < high:
        if a[i] == 0:
            a[low], a[i] = a[i], a[low]
            low += 1
        if a[i] == 2:
            a[high], a[i] = a[i], a[high]
            high -= 1; i -= 1
        i += 1

    print(a)

dutch(arr)

