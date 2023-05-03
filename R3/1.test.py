haystack = "WELCOMETOSURANACOLLEGE"
needle = "SURANA"

def find():
    #make bad match table
    d = {}; m = len(needle)
    for i in range(len(needle)):
        d[needle[i]] = m - i - 1

    d['*'] = m
    d[needle[m-1]] = m

    print(d)

    tempm = m; i = 0
    while i + tempm - 1 < len(haystack) and tempm > 0:
        if haystack[i+tempm-1] == needle[tempm - 1]:
            tempm -= 1
        else:
            if haystack[i+m-1] in d.keys():
                i += d[haystack[i+m-1]]
            else:
                i += d['*']
            tempm = m
        
    if tempm:
        print('-1')
    else:
        print(i)
        return
find()
