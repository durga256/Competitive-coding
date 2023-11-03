S1 = 'clrwmpkwru'; S2 = 'wmpkwruclr'

def ble():
    d = {}; n = len(S1)
    for i in range(len(S1)):
        if S1[i] not in d.keys():
            d[S1[i]] = set()
            d[S1[i]].add(S1[i-1])
            d[S1[i]].add(S1[(i+1)%n])
        else:
            d[S1[i]].add(S1[i-1])
            d[S1[i]].add(S1[(i+1)%n])

    print(d)

    for i in range(len(S2)):
        if S2[i] not in d.keys():
            return False
        else:
            if S2[i-1] not in d[S2[i]] or S2[(i+1)%n] not in d[S2[i]]:
                return False
    
    return True

print(ble())
        