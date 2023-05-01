haystack = "sadbutsad"; needle = "sad"

def rabin():
    m = len(needle)
    s2_hash = 0
    for i in range(len(needle)):
        s2_hash += (ord(needle[i]) - 96)*(26**(m-i-1))
        print(s2_hash)

    res = []
    #first window
    s1_hash = 0
    for i in range(m):
        s1_hash += (ord(haystack[i]) - 96)*(26**(m-i-1))

    if s2_hash == s1_hash: #for case where len(haystack) == len(needle) => 
        res.append(0)      #next for loop will never run

    for i in range(len(haystack)-m):
        s1_hash -= (ord(haystack[i])-96)*(26**(m-1))
        s1_hash *= 26
        s1_hash += ord(haystack[i+m])-96
        if s1_hash == s2_hash:
            res.append(i+1)

    print(res)


    print(s2_hash)

rabin()


