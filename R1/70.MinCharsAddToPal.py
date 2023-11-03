s = "AACECAAAA"

def f():
    n = len(s)
    start = res = 0; end = n-1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            res += 1
            start = 0
            end = n-res-1

    return res

print(f())
