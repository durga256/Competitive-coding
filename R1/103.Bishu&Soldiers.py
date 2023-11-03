#https://codeforces.com/contest/1888/problems - problem 1

import sys
sys.stdin = open('CodeForces/input.txt', 'r')
sys.stdout = open('CodeForces/output.txt', 'w')

def getInput():
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))
    #arr = [int(x) for x in input().split()]  
    Q = int(input())
    power_rounds = []
    for i in range(Q):
        power_rounds.append(int(input()))

    return (N, arr, Q, power_rounds)

def binary_search(arr,low,high,k):
    if low <= high:
        mid = (high-low)//2+low

        if (mid == len(arr)-1 or arr[mid+1]> k) and arr[mid] <= k:
            return mid
        elif arr[mid] <= k:
            return binary_search(arr, mid+1, high, k)
        else:
            return binary_search(arr, low, mid-1, k)
    return -1

def f():
    N, arr, Q, power_rounds = getInput()
    arr.sort()
    for i in range(Q):
        idx = binary_search(arr, 0, len(arr)-1, power_rounds[i])
        print(idx+1, sum(arr[:idx+1]))

f()
