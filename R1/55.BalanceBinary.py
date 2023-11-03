s = '0100110101'
s = "0111100010"

def f():
    ones = 0; zeros=0; res = []; start = 0
    for i in range(len(s)):
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1
        if ones == zeros:
            res.append(s[start:i+1])
            ones = 0; zeros = 0
            start = i+1

    if start == len(s):
        return len(res)
    else:
        return -1

print(f())