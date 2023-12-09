str1 = "BA"
str2 = "XYZ"
shuffle = "ABYXZ"

def f():
    d = {}

    for i in str1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in str2:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in shuffle:
        if i not in d or d[i] <= 0:
            return False
        if i in d:
            d[i] -= 1

    for i in d:
        if d[i]:
            return False
    return True

print(f())