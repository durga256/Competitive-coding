arr = [5, 20, 3, 2, 50, 80]; n = 78

def f():
    d = {}

    for i in range(len(arr)):
        d[arr[i]] = 1

    for i in range(len(arr)):
        if arr[i] + n in d:
            return True
        
    return False

def f2():
    def bin_search(arr, k, idx):
        l = 0; h = len(arr)-1
        while l <= h:
            mid = (l+h)//2
            if (arr[mid] == k and mid != idx):
                return arr[mid]
            elif arr[mid] > k:
                h = mid - 1
            else:
                l = mid + 1
                
        return -1
                
    arr.sort()
    for i in range(len(arr)):
        temp = bin_search(arr, abs(N-arr[i]), i)
        if temp != -1:
            return True
            
    return False

f2()
        
    