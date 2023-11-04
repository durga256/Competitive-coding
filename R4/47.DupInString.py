S = 'geeksforgeeks'

def f():
    d = {}
    res = set()
    for i in range(len(S)):
        if S[i] in d:
            res.add(S[i])
        d[S[i]] = 1

    print(res)

f()