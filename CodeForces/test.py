import sys

sys.stdin = open('CodeForces/input.txt',  'r')

from collections import Counter
def get_input():
    n = int(input())
    tc = []
    for i in range(n):
        tc.append(input())
    return tc

def f():
    tc = get_input()
    for i in tc:
        d = Counter(i)
        if 'A' not in d:
            print('B')
        elif 'B' not in d:
            print('A')
        elif d['A'] > d['B']:
            print('A')
        else:
            print('B')
    
f()


