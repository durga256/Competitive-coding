import sys

sys.stdin = open('CodeForces\input.txt', 'r')
sys.stdout = open('CodeForces\output.txt', 'w')

def get_input():
    n, k = input().split()
    n = int(n); k = int(k)

    arr = [int(x) for x in input().split()]

    return (arr, n, k)

def ok(arr, mid_val, cows):
    
    n = len(arr)

    d = arr[0]; count = 1 #already placing a cow
    for i in range(n):
        if arr[i] - d >= mid_val:
            d = arr[i]
            count += 1
    
    if count >= cows:
        return True
    return False


def f():
    arr, n, k = get_input()

    arr.sort()
    l = arr[0]-1; r = arr[n-1]+1; ans = 1
    while l <= r:
        mid = l+(r-l)//2

        if ok(arr, mid, k):
            ans = mid
            l = mid+1
        else:
            r = mid - 1

    print(arr)
    print(ans)

f()