import sys
sys.stdin = open('CodeForces/input.txt', 'r')
sys.stdout = open('CodeForces/output.txt', 'w')

def getInput():
    TC = []
    for i in range(int(input())):
        N, Q = input().split()
        ranges = []
        queries = []
        for j in range(int(N)):
            ranges.append([int(x) for x in input().split()])
        ranges.sort()
        for j in range(int(Q)):
            queries.append(int(input()))
        TC.append([ranges, queries])

    return TC

def f():
    TC = getInput()
    output = []

    for i in range(len(TC)):
        ranges = TC[i][0]
        queries = TC[i][1]
        final_range = []
        for j in range(len(ranges)):
            if final_range and ranges[j][0] <= final_range[-1][1]:
                final_range[-1][1] = max(final_range[-1][1],ranges[j][1])
            else:
                final_range.append(ranges[j])

        for j in range(len(queries)):
            k = 0; op = -1; temp_q = queries[j]
            while k < len(final_range):
                if final_range[k][0]+temp_q-1 <= final_range[k][1]:
                    op = final_range[k][0]+temp_q-1
                    break
                else:
                    temp_q -= final_range[k][1]
                    temp_q += final_range[k][0]-1
                    k += 1
            output.append(op)

    for i in output:
        print(i)

f()