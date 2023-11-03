s = "Ravi had been saying that he had been there"

def f(s):
    d = {}
    s = s.split(' ')
    for i in range(len(s)):
        if s[i] in d:
            return s[i]
        d[s[i]] = 1

    return 'No repeat'

print(f(s))