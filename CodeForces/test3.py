import sys

sys.stdin = open('CodeForces/input.txt',  'r')

def get_input():
    n = int(input())
    tc = []
    for i in range(n):
        tc.append(int(input()))

    return tc

def f():
    tc = get_input()
    #print(tc)
    
    for i in tc:
        if i <= 9:
            ans = 0
            for j in range(1,i+1):
                ans += j
            print(ans)
        else:
            ans = 45
            temp = 10
            j = 55
            while temp+10 <= i:
                ans += j
                temp += 10
                j += 10
                if temp % 100 == 0:
                    j = 55
                    rem = 0
                    if temp >= 100000:
                        rem += temp//100000
                        rem += int(str(temp)[1:])//10000
                        rem += int(str(temp)[2:])//1000
                        rem += int(str(temp)[3:])//100
                    elif temp >= 10000:
                        rem += temp//10000
                        rem += int(str(temp)[1:])//1000
                        rem += int(str(temp)[2:])//100
                    elif temp >= 1000:
                        rem += temp//1000
                        rem += int(str(temp)[1:])//100
                    elif temp >= 100:
                        rem += temp//100
                    j += (rem-1)*10
            while temp <= i:
                ans += sum([int(x) for x in str(temp)])
                temp += 1
            print(ans)

f()
# print(sum([x for x in range(1,11)]))
# print(sum([x for x in range(2,12)]))
# print(sum([x for x in range(3,13)]))
# print(sum([x for x in range(4,14)]))
# print(sum([x for x in range(5,15)]))
# print(sum([x for x in range(6,16)]))
# print(sum([x for x in range(7,17)]))
# print(sum([x for x in range(8,18)]))
# print(sum([x for x in range(9,19)]))
# print(sum([x for x in range(18,28)]))
# j = 55
# print(9900//1000)
# for k in range(1,18):
#     j += 10
# print(j)
# print(17*10+55)