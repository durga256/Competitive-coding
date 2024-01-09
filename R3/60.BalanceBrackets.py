#no.of operations to make unbalanced brackets balanced
exp = "}{{}}{{{"
#exp = "{{}{{{}{{}}{{"
exp = "}{}}}}{{}{}}{}{}{{{{}{}}{}}}{{}}}}}}{"

def f():
    temp = 0; res = 0
    for i in exp:
        if i == '{':
            temp += 1
        else:
            if temp == 0:
                res += 1
                temp += 1
            else:
                temp -= 1

    print(res, temp)
    if temp % 2 != 0:
        return -1
    if temp != 0:
        res += temp //2

    print(res)

f()