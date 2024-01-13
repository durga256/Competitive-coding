s = "AACECAAAA"

def f():
    n = len(s)
    s = s + '*' + s[::-1]
    m = len(s)
    prev_idx = 0; i = 1
    lps = [0]*m
    while i < m:
        if s[i] == s[prev_idx]:
            prev_idx += 1
            lps[i] = prev_idx
            i += 1
        else:
            if prev_idx == 0:
                lps[i] = 0
                i += 1
            else:
                prev_idx = lps[prev_idx-1]

    return n-lps[-1]

print(f())
