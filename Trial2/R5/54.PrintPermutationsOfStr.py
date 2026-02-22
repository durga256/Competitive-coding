s="ABC"

def f(s,l,r):
    if l == r:
        print(''.join(s))
    else:
        for i in range(l,r):
            s[l], s[i] = s[i], s[l]
            f(s,l+1,r)
            s[l],s[i] = s[i], s[l]

f(list(s),0,len(s))
