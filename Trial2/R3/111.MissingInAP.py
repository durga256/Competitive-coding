arr  = [2, 4, 8, 10, 12, 14]

arr = [14,12,10,8,4,2]
arr = [49, 59, 69, 79, 89, 99, 109, 129]

def f():
    n = len(arr)
    #an = a0 + (n-1)d
    d = (arr[-1] - arr[0])//n
    l = 0; h = len(arr)-1
    while l <= h:
        mid = (l+h)//2
        print(arr[mid])
        if (mid == 0 or arr[mid-1] == arr[0]+(mid-1)*d) and arr[mid] != arr[0]+(mid)*d:
            return arr[0]+(mid)*d
        elif arr[mid] == arr[0]+(mid-1)*d:
            l = mid + 1
        else:
            h = mid - 1
    
print(f())

def findMissing(self, arr, n):
    # code here
    d = (arr[n-1]-arr[0])//n
    
    ideal_sum = (n+1)*(2*arr[0]+n*d)//2
    
    return ideal_sum - sum(arr)