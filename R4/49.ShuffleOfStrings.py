str1 = "BA"
str2 = "XYZ"
shuffle = "ABYX"

def s():
    d = {}
    for i in range(len(str1)):
        if str1[i] in d:
            d[str1[i]] += 1
        else:
            d[str1[i]] = 1

    for i in range(len(str2)):
        if str2[i] in d:
            d[str2[i]] += 1
        else:
            d[str2[i]] = 1

    for i in range(len(shuffle)):
        if shuffle[i] not in d or d[shuffle[i]] <= 0:
            return False
        d[shuffle[i]] -= 1

    for i in d:
        if d[i] > 0:
            return False
        
    return True

print(s())

