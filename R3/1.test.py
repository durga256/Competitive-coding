P = 12222333
#P = 1234

def next():
    n = str(P)
    n = list(n)
    pivot_idx = -1
    for i in range(len(n)-1,0,-1):
        if n[i] > n[i-1]:
            pivot_idx = i - 1
            break

    if pivot_idx == -1:
        return pivot_idx
    
    min_index = pivot_idx + 1
    for i in range(pivot_idx+2, len(n)):
        if n[i] > n[pivot_idx] and n[i] <= n[min_index]:
            min_index = i

    n[pivot_idx], n[min_index] = n[min_index], n[pivot_idx]

    n[pivot_idx+1:] = reversed(n[pivot_idx+1:])
    res = ""
    for i in n:
        res += i
    print(res)
    print(int(res))

next()