import sys

sys.stdin = open('CodeForces\input.txt', 'r')
sys.stdout = open('CodeForces\output.txt','w')

def get_input():
    tc = int(input())

    tcs = []
    for i in range(tc):
        order = int(input())
        cooks_rank = [int(x) for x in input().split()]
        cooks_rank.pop(0)
        tcs.append([order, cooks_rank])

    return tcs

def ok(arr, time, order):
    all_cooks_work = 0
    for i in range(len(arr)):
        time_now = arr[i]
        count = 0
        val = 1
        while time_now <= time:
            count += 1
            val += 1
            time_now += val*arr[i]

        all_cooks_work += count

        if all_cooks_work >= order:
            return True
    return False

def f():
    tcs = get_input()
    
    for i in tcs:
        order = i[0]
        cook_ranks = i[1]
        cook_ranks.sort()
        l = 1; r = cook_ranks[len(cook_ranks)-1]*(order*(order+1)//2)

        while l <= r:
            mid = l+(r-l)//2

            temp = ok(cook_ranks, mid, order)
            if temp:
                ans = mid
                r = mid-1
            else:
                l = mid+1

        print(ans)

f()