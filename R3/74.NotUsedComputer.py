def f(n,s):
    waitList = set()
    seated = set(); res = 0
    for i in range(len(s)):
        if s[i] not in seated and len(seated) < n:
            seated.add(s[i])
        elif s[i] not in seated and s[i] not in waitList:
            waitList.add(s[i])
        elif s[i] in seated:
            seated.remove(s[i])
        elif s[i] in waitList:
            waitList.remove(s[i])
            res += 1
        print("Seated: ",seated)
        print("WaitList: ", waitList)
    print(res)

#f(2, 'ABBAJJKZKZ')

def f2(n,s):
    d = {}; occupied = 0; res = 0
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1

            if occupied < n:
                occupied += 1
                d[s[i]] = 2
            else:
                res += 1
        else:
            if d[s[i]] == 2:
                occupied -= 1
            d[s[i]] == 0
        print(d)

    print(res)

f2(2, 'ABBAJJKZKZ')
f2(3, "GACCBDDBAGEE")
f2(3, "GACCBGDDBAEE")
f2(1, "ABCBCA")
f2(1, "ABCBCADEED")