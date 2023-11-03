arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5

arr1 = [5, 5, 8, 8, 8, 9, 11, 11, 11, 11, 11]
arr2 = [4, 4, 4, 4, 6, 8, 9, 9, 9, 11, 13]
k = 2

def f(arr1,n,arr2,m,k):
    if k > m+n or k < 1:
        return -1
    
    if m > n:
        return f(arr2,m,arr1,n,k)
    
    if m == 0:
        return arr2[k-1]
    
    if k == 1:
        return min(arr1[0], arr2[0])
    
    i = min(m, k//2)
    j = min(n, k//2)

    if arr1[i-1] > arr2[j-1]:
        return f(arr1, n, arr2[j:], m-j, k-j)
    else:
        return f(arr1[i:], n-i, arr2, m, k-i)
    
print(f(arr1,len(arr1), arr2, len(arr2), k))