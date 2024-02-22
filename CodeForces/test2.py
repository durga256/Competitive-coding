import sys

sys.stdin = open('CodeForces/input.txt',  'r')
def get_input():
    n = int(input())
    tc = []
    for i in range(n):
        x = int(input())
        temp = []
        for j in range(x):
            temp.append(input())
        tc.append(temp)

    return tc

def f():
    tc = get_input()
    for arr in tc:
        prev = None
        temp = None
        for i in arr:
            if '1' not in i:
                continue
            elif not prev:
                prev = 0
                for j in i:
                    if j == '1':
                        prev += 1
            else:
                temp = 0
                for j in i:
                    if j == '1':
                        temp += 1
                if temp == prev:
                    print('SQUARE')
                else:
                    print('TRIANGLE')
                break

f()