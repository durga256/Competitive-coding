import sys

sys.stdin = open('CodeForces/input.txt', 'r')
sys.stdout = open('CodeForces/output.txt', 'w')

def get_input():
    tc = []
    while True:
        a = [int(i) for i in input().split()]
        if a[0] == 0:
            break
        a.pop(0)
        tc.append(a)

    return tc

def f():
    tc = get_input(); i = 0
    while i < len(tc)-1:
        First = tc[i]
        Second = tc[i+1]
        p = 0; q = 0; sum1 = 0; sum2 = 0; total_sum = 0
        while p < len(First) and q < len(Second):
            if First[p] == Second[q]:
                total_sum += max(sum1, sum2)
                total_sum += First[p]
                sum1 = sum2 = 0
                p += 1; q += 1
            elif First[p] < Second[q]:
                sum1 += First[p]
                p += 1
            else:
                sum2 += Second[q]
                q += 1

        while p < len(First):
            sum1 += First[p]
            p += 1

        while q < len(Second):
            sum2 += Second[q]
            q += 1

        total_sum += max(sum1, sum2)
            
        i += 2
        print(total_sum)



f()