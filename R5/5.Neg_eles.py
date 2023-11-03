arr = [-7,-8,-90,7,6,-56,87,80,-87]

def right_rotate(a,i,j):
    temp = a[j]
    for k in range(j-1, i-1, -1):
        a[k+1] = a[k]

    a[i] = temp
    return a


def neg_eles(a):
    i = 0; low = 0
    while a[low] < 0:
        low += 1
    
    i = low
    while i < len(a):
        if a[i] < 0:
            a = right_rotate(a, low, i)
            low += 1
        i += 1
        print(a)

neg_eles(arr)

