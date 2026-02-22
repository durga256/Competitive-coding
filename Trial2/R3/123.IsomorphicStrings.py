def f(s1,s2):

    if len(s1) != len(s2):
        return False
    d = {}
    for i in range(len(s1)):
        if s1[i] in d and s2[i] != d[s1[i]]:
            return False
        else:
            d[s1[i]] = s2[i]

    if len(set(d.values())) != len(d):
        return False
    
    return True


f('abc','xyy')