def isPossible(arr,n,m,curr_min):
    studentsRequire = 1
    curr_sum = 0
    for i in range(n):

        if arr[i] > curr_min:
            return False
        
        if curr_sum + arr[i] > curr_min:

            studentsRequire += 1

            curr_sum = arr[i]

            if studentsRequire > m:
                return False
        else:
            curr_sum += arr[i]
            
    return True

def finf(arr, m):
    total_pages = sum(arr)
    n = len(arr)

    if m > len(arr):
        return -1

    start = 0; end = total_pages
    while start <= end:
        mid = (start+end)//2

        if isPossible(arr, n, m, mid):
            result = mid
            end = mid - 1

        else:
            start = mid+1

    print(result)

finf([12, 34, 67, 90], 5)
finf([10,10,10,10], 2)
finf([5,10,30,20,15],3)