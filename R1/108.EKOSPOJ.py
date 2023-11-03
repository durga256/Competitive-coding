import sys
sys.stdin = open('CodeForces/input.txt', 'r')
sys.stdout = open('CodeForces/output.txt', 'w')

def getInput():
    N, H = input().split()

    trees = [int(x) for x in input().split()]

    return (trees, int(H))

def find(arr, H):
    n = len(arr)
    s = 0
    e = arr[n-1]
    mid = s+(e-s)//2
    while s <= e:
        count = 0
        for i in range(n):
            if arr[i] > mid:
                count += arr[i]-mid

        if count >= H:
            answer = mid
            s = mid+1
        else:
            e = mid-1
        mid = s + (e-s)//2
    return answer

def f():
    trees, H = getInput()

    d = {}
    trees.sort()

    print(find(trees, H), end="")

f()