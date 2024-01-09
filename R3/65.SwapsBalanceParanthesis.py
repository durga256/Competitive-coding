s = "]]][[["

def f():
    temp = 0; res = 0
    for i in range(len(s)):
        if s[i] == '[':
            temp += 1
        else:
            if temp == 0:
                res += 1
                temp += 1
            else:
                temp -= 1

    print(res)

f()