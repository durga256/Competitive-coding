#no.of operations to make unbalanced brackets balanced
exp = "}{{}}{{{"

def f():
    temp = 0; res = 0
    for i in range(len(exp)):
        if exp[i] == '{':
            temp += 1
        else:
            if temp == 0:
                res += 1
                temp += 1
            else:
                temp -= 1

    if temp:
        res += temp //2

    print(res)

f()
