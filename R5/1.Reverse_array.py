arr = [1,2,3,4,5,6,7]

def reverse_arr(a):
    n = len(a)
    for i in range(int(n/2)):
        a[i], a[n-i-1] = a[n-i-1], a[i]

    return a
    #return a[::-1]

print(reverse_arr(arr))