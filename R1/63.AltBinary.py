s = "111000"

def flip(ch):
    if ch == '1':
        return '0'
    return '1'

def f(s,expected):
    flipCount = 0
    for i in range(len(s)):
        if s[i] != expected:
            flipCount += 1

        expected = flip(expected)

    return flipCount

print(min(f(s,'1'),f(s,'0')))