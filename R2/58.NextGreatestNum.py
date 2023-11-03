n = "218765"
n = [2,2,7,5,4,3,2,2,1]
n = [1,2,0,3,0,1,2,4]

def p(arr,l,h):
    if l <= h:
        mid = (l+h)//2

        if mid <h  and arr[mid+1] > arr[mid]:
            return mid
        elif mid > l and arr[mid-1] < arr[mid]:
            return mid-1
        if arr[l] > arr[mid]:
            return 
        return p(arr,l, mid-1)
    return -1

def f(n):
    n = [x for x in list(n)]
    print(n)
    n_len = len(n); pivot_idx = -1
    pivot_idx = p(n,0,n_len-1)
    print(pivot_idx)
    # for i in range(n_len-1,0,-1):
    #     if n[i] > n[i-1]:
    #         pivot_idx = i-1
    #         break

    if pivot_idx == -1:
        n[:]=reversed(n[:])
        return ''.join([str(x) for x in n])
    
    min_idx = pivot_idx+1
    for i in range(pivot_idx+1,n_len):
        if n[i] > n[pivot_idx] and n[i] <= n[min_idx]:
            min_idx = i

    n[pivot_idx], n[min_idx] = n[min_idx], n[pivot_idx]
    n = [str(x) for x in n]
    n[pivot_idx+1:] = reversed(n[pivot_idx+1:])
    return ''.join(n)

print(f(n))