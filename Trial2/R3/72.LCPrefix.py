d = ['geeksforgeeks', 'geeks', 'geek', 'geezer']

def f():
    min_len = min(list(map(len,d)))
    res = ""
    for i in range(min_len):
        s = d[0][i]
        for string in d:
            if string[i] != s:
                return res
        res += s
    return res

print(f())
