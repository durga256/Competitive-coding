import sys
arr = [1, 4, 45, 6, 0, 19]; x  =  51
x = 7; arr = [2,3,1,2,4,3]

def minSub():
    start = 0; end = 0; subSum = 0; minLen = len(arr)
    while end < len(arr):
        while subSum <= x and end < len(arr):
            subSum += arr[end]
            end += 1

        while start < len(arr) and subSum > x:
            minLen = min(minLen, end - start)
            subSum -= arr[start]
            start += 1
        
        end = start

    if minLen == len(arr):
        return 0
    return minLen

        
