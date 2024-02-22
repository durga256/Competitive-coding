import sys

sys.stdin = open('CodeForces/input.txt',  'r')

def get_input():
    n = int(input())
    tc = []
    for i in range(n):
        tc.append([int(x) for x in input().split()])
    return tc

def f():
    tc = get_input()
    for i in tc:
        num_cards, k = i
        temp = set()
        for j in range(1,num_cards+1):
            temp.add(j)
        multiplier = 1
        curr_k = 0
        while curr_k < k:
            starter = 1
            while starter*multiplier <= num_cards:
                if curr_k == k-1:
                    print(starter*multiplier)
                    break
                if starter*multiplier in temp:
                    temp.remove(starter*multiplier)
                    starter += 2
                    curr_k += 1
                else:
                    starter += 2
            multiplier += 1



f()
